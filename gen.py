from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import os
from dotenv import load_dotenv
from pynytimes import NYTAPI
from sentence_transformers import SentenceTransformer
from annoy import AnnoyIndex
import numpy as np
import time
from tqdm import tqdm
import schema
import util

load_dotenv()

API_KEY = os.getenv("NYT_KEY") or ""
nyt = NYTAPI(API_KEY, parse_dates=True)

model = SentenceTransformer("sentence-transformers/sentence-t5-base")
EMBED_LENGTH = 768

# TODO: More research on what the best value of this might be
NUM_TREES = 10


def get_vec(sentence: str) -> np.ndarray:
    """
    Helper method to embed a sentence as a 1 dimenstional vector
    :param str sentence: What to embed
    """
    return np.array(model.encode(sentence)).flatten()


def get_vecs(sentences: list[str]) -> np.ndarray:
    """
    Helper method to embed sentences as a 1 dimensional vector
    :param list[str] senteces: What to embed
    """
    return np.array(model.encode(sentences))


dbman = schema.DBManager("meta.db")

START_DATE = datetime(2004, 1, 1)
END_DATE = datetime(2005, 12, 31)

# How many articles to embed at oncc
BATCH_SIZE = 64

# NOTE: Hacking to get the ix data again


# Fetching the dates
def main_loop():
    dates: list[datetime] = []
    date = START_DATE
    while date < END_DATE:
        dates.append(date)
        date += relativedelta(months=1)
    for ix, date in enumerate(dates):
        print(f"{ix + 1}/{len(dates)}")
        # Make the indexes
        abs_ix = AnnoyIndex(EMBED_LENGTH, "angular")
        head_ix = AnnoyIndex(EMBED_LENGTH, "angular")
        par_ix = AnnoyIndex(EMBED_LENGTH, "angular")
        start_time = datetime.now()
        # Get the data
        data = nyt.archive_metadata(date)
        # Get the embeddings and update the indexes
        for ix, article in tqdm(enumerate(data), total=len(data)):
            # Get each embedding and add to index
            abs_emb = get_vec(article["abstract"])
            abs_ix.add_item(ix, abs_emb)
            head_emb = get_vec(article["headline"]["main"])
            head_ix.add_item(ix, head_emb)
            par_emb = get_vec(article["lead_paragraph"])
            par_ix.add_item(ix, par_emb)
            # Add the article metadata to the DB so it can be retrieved later
            meta = schema.Article(
                id=article["_id"],
                month=util.month_to_str(date),
                annoy_ix=ix,
                abstract=article["abstract"],
                headline=article["headline"]["main"],
                lead_paragraph=article["lead_paragraph"],
            )
            dbman.add_article(meta)
        dbman.con.commit()
        end_time = datetime.now()
        diff = end_time - start_time
        if diff.seconds < 5:
            time.sleep(diff.seconds)
        # Build and save the models
        model_name = f"{util.month_to_str(date)}.ann"
        abs_ix.build(NUM_TREES, n_jobs=-1)
        abs_ix.save(f"models/abs/a_{model_name}")
        head_ix.build(NUM_TREES, n_jobs=-1)
        head_ix.save(f"models/head/h_{model_name}")
        par_ix.build(NUM_TREES, n_jobs=-1)
        par_ix.save(f"models/par/p_{model_name}")


if __name__ == "__main__":
    main_loop()

"""
aix = AnnoyIndex(EMBED_LENGTH, "angular")
aix.load("models/head/h_01-01-2001.ann")

while True:
    date = "01-2001"
    sentence = input("Input a sentence: ")
    if sentence == "":
        break
    emb = get_vec(sentence)
    for ix in aix.get_nns_by_vector(emb, 10):
        article = dbman.get_article_by_month_and_ix(date, ix)
        if article is None:
            print("WHAT! No results")
        else:
            print(article.headline)
"""
