"""
The goal of this script is to run our analysis and produce a new
`api.py` file which will be used to serve our website. This involves:
- Fetching todays news articles (say top 10)
- Running our analysis on them and finding the most similar from our models
- Generating a new `api.py` file with the results
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
from gen import EMBED_LENGTH, get_vec
from schema import DBManager, Article
from typing import Union, NamedTuple
from sentence_transformers import SentenceTransformer

# Housekeeping
load_dotenv()

API_KEY = os.getenv("NYT_KEY")
DB_FILE = "meta.db"

nyt = NYTAPI(API_KEY or "", parse_dates=True)

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

    def to_api_str(self) -> str:
        """
        Convert this article to a string that can be used in the api
        """
        return f"""FrontendArticle(
            title="{self.title}",
            abstract="{self.abstract}",
            img_url="{self.img_url}",
            article_url="{self.article_url}",
            date_str="{self.date_str}"
        )"""


# Load today's news
print("Getting top stories...")
top_stories = nyt.top_stories()

# Get all of the annoy indexes into memory
print("Loading annoy indexes...")
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
print("Loading database...")
dbman = DBManager(DB_FILE)

# Run the analysis
print("Showing crazy cynical things...")
results: list[tuple[FrontendArticle, FrontendArticle]] = []

"""
FOR TESTING
results = [
    (
        FrontendArticle(
            title="The title",
            abstract="The abstract",
            img_url="https://upload.wikimedia.org/wikipedia/commons/b/bd/Test.svg",
            article_url="https://www.nytimes.com/2021/05/02/us/politics/biden-100-days.html",
            date_str="April 1st, 2004",
        ),
        FrontendArticle(
            title="The title",
            abstract="The abstract",
            img_url="https://upload.wikimedia.org/wikipedia/commons/b/bd/Test.svg",
            article_url="https://www.nytimes.com/2021/05/02/us/politics/biden-100-days.html",
            date_str="May 10th, 2023",
        ),
    ),
]
"""

for story in tqdm(top_stories):
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
    full_old_article = nyt.article_search(
        query=min_article.headline,
        results=1,
        dates={"begin": datetime(2000, 1, 1), "begin": datetime(2006, 1, 1)},
    )
    full_old_article = full_old_article[0] if len(full_old_article) > 0 else None
    if full_old_article is None:
        continue
    old_article = FrontendArticle(
        title=full_old_article["headline"]["main"],
        abstract=full_old_article["abstract"],
        img_url="https://static01.nyt.com/" + full_old_article["multimedia"][0]["url"]
        if len(full_old_article["multimedia"]) > 0
        else None,
        article_url=full_old_article["web_url"],
        date_str=min_date,
    )
    new_article = FrontendArticle(
        title=story["title"],
        abstract=story["abstract"],
        img_url=story["multimedia"][0]["url"] if len(story["multimedia"]) > 0 else None,
        article_url=story["url"],
        date_str=month_to_str(story["created_date"]),
    )
    results.append((old_article, new_article))

# Create a new api.py file for deployment
print("Writing api.py...")
with open("test_api.py", "w") as f:
    results_str = "results = [\n"
    for result in results:
        results_str += "    (\n"
        results_str += "        " + result[0].to_api_str() + ",\n"
        results_str += "        " + result[1].to_api_str() + "\n"
        results_str += "    ),\n"
    results_str += "]\n"
    f.write(
        f"""# THIS IS AN AUTO-GENERATED FILE. DO NOT EDIT
from flask import Flask, render_template
from typing import Union, NamedTuple

app = Flask(__name__)


class FrontendArticle(NamedTuple):
    title: str
    abstract: str
    img_url: Union[str, None]
    article_url: str
    date_str: str


{results_str}
@app.route("/")
def index():
    return render_template("index.html", results=results)
"""
    )
