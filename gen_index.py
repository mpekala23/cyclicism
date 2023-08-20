"""
The goal of this script is to run our analysis and produce a new
`index.html` file which will be used to serve our website. This involves:
- Fetching todays news articles (say top 10)
- Running our analysis on them and finding the most similar from our models
- Generating a new `index.html` file with the results
"""
print("Houeskeeping...")
import numpy as np
from pynytimes import NYTAPI
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import os
from dotenv import load_dotenv
from pynytimes import NYTAPI
from annoy import AnnoyIndex
from tqdm import tqdm
from util import month_to_str, str_to_month
from schema import DBManager, Article
from typing import Union, NamedTuple
from sentence_transformers import SentenceTransformer
from google_images_search import GoogleImagesSearch
import random
from flask import Flask, render_template
import logging
import time

# Setup quality-of-life logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=f"/Users/mork/Desktop/projects/cyclicism/logs/{int(time.time())}.log",
    filemode="a",
)
logger = logging.getLogger(__name__)

# Housekeeping
load_dotenv()

API_KEY = os.getenv("NYT_KEY")
DB_FILE = "meta.db"

nyt = NYTAPI(API_KEY or "", parse_dates=True)
GOOGLE_KEY = os.getenv("GOOGLE_KEY") or ""
gis = GoogleImagesSearch(GOOGLE_KEY, "a708aeeac07f04808")

model = SentenceTransformer("sentence-transformers/sentence-t5-base")
EMBED_LENGTH = 768


def get_vec(sentence: str) -> np.ndarray:
    """
    Helper method to embed a sentence as a 1 dimenstional vector
    :param str sentence: What to embed
    """
    return np.array(model.encode(sentence)).flatten()


def get_closest_for_date(
    abs_emb: np.ndarray, head_emb: np.ndarray, date: str
) -> tuple[Union[Article, None], float]:
    """
    For a given month, return the closest article and its distance.
    To calculate this, we use the abstract embedding to get the closest 5
    articles.
    """
    min_article = None
    min_dist = float("inf")
    ixs, dists = month_to_aix[date].get_nns_by_vector(
        abs_emb, 3, include_distances=True
    )
    for ix, dist in zip(ixs, dists):
        article = dbman.get_article_by_month_and_ix(date, ix)
        if article is None:
            continue
        head_vec = get_vec(article.headline)
        dist += np.linalg.norm(head_emb - head_vec)
        if dist < min_dist:
            min_dist = dist
            min_article = article
    return min_article, min_dist


class FrontendArticle(NamedTuple):
    """
    A class to represent an article that will be sent to the frontend
    """

    title: str
    abstract: str
    img_url: Union[str, None]
    article_url: str
    date_str: str


# Load today's news
logger.info("Getting top stories...")
top_stories = nyt.top_stories()

# Get all of the annoy indexes into memory
logger.info("Loading annoy indexes...")
start_date = datetime(2001, 1, 1)
end_date = datetime(2005, 12, 31)

month_to_aix = {}
month_to_hix = {}
month_to_pix = {}
date = start_date
while date < end_date:
    mstr = month_to_str(date)
    aix_file = f"models/abs/a_{mstr}.ann"
    hix_file = f"models/head/h_{mstr}.ann"
    pix_file = f"models/par/p_{mstr}.ann"
    aix = AnnoyIndex(EMBED_LENGTH, "angular")
    hix = AnnoyIndex(EMBED_LENGTH, "angular")
    pix = AnnoyIndex(EMBED_LENGTH, "angular")
    aix.load(aix_file)
    hix.load(hix_file)
    pix.load(pix_file)
    month_to_aix[mstr] = aix
    month_to_hix[mstr] = hix
    month_to_pix[mstr] = pix
    date += relativedelta(months=1)

# Load the database
logger.info("Loading database...")
dbman = DBManager(DB_FILE)

# Run the analysis
logger.info("Showing crazy cynical things...")
results: list[tuple[FrontendArticle, FrontendArticle]] = []

for story in tqdm(top_stories[:15]):
    try:
        min_article: Union[Article, None] = None
        min_date = ""
        min_dist = float("inf")
        title = story["title"]
        abstract = story["abstract"]
        for date, aix in month_to_aix.items():
            abs_emb = get_vec(abstract)
            head_emb = get_vec(title)
            article, dist = get_closest_for_date(abs_emb, head_emb, date)
            if article is None:
                continue
            if dist < min_dist:
                min_dist = dist
                min_article = article
                min_date = date
        if min_article is None:
            continue
        _search_params = {
            "q": min_article.headline,
            "num": 5,
            "fileType": "jpg",
            "safe": "active",
        }
        gis.search(search_params=_search_params)
        searched_imgs = gis.results()
        old_img_url = min_article.img_url
        if len(searched_imgs) > 0:
            old_img_url = random.choice(searched_imgs).url
        old_article = FrontendArticle(
            title=min_article.headline,
            abstract=min_article.abstract[:176],
            img_url=old_img_url,
            article_url=min_article.web_url,
            date_str=str_to_month(min_date).strftime("%B %Y"),
        )
        new_article = FrontendArticle(
            title=story["title"],
            abstract=story["abstract"][:176],
            img_url=story["multimedia"][0]["url"] if len(story["multimedia"]) > 0 else None,
            article_url=story["url"],
            date_str=story["created_date"].strftime("%B %Y"),
        )
        results.append((old_article, new_article))
    except Exception as e:
        logger.warning(f"Exception: {e.args}")

# Create a new index.html file for deployment
logger.info("Writing index.html...")

app = Flask(__name__)

with open("index.html", "w") as fout, app.app_context(), app.test_request_context():
    fout.write(render_template("index.html", results=results))

logger.info("Pushing to git")
os.system(f"cd /Users/mork/Desktop/projects/cyclicism && git add . && git commit -m 'update at {int(time.time())}' && git push")
