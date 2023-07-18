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

load_dotenv()

API_KEY = os.getenv("NYT_KEY") or ""
nyt = NYTAPI(API_KEY, parse_dates=True)

model = SentenceTransformer("sentence-transformers/sentence-t5-base")
EMBED_LENGTH = 768

NUM_TREES = 36


def get_vec(sentence: str):
    return np.array(model.encode(sentence)).flatten()


# Fetching the dates
def main_loop():
    dates = []
    date = datetime(2001, 1, 1)
    while date < datetime.now() - timedelta(days=365 * 10):
        dates.append(date)
        date += relativedelta(months=1)
        break
    for ix, date in enumerate(dates):
        print(f"{ix + 1}/{len(dates)}")
        # Make the indexes
        abs_ix = AnnoyIndex(EMBED_LENGTH, "angular")
        head_ix = AnnoyIndex(EMBED_LENGTH, "angular")
        par_ix = AnnoyIndex(EMBED_LENGTH, "angular")
        start_time = datetime.now()
        # Get the data
        data = nyt.archive_metadata(date)
        for ix, article in tqdm(enumerate(data[:3]), total=len(data)):
            # Get each embedding and add to index
            abs_emb = get_vec(article["abstract"])
            abs_ix.add_item(ix, abs_emb)
            head_emb = get_vec(article["headline"]["main"])
            head_ix.add_item(ix, head_emb)
            par_emb = get_vec(article["lead_paragraph"])
            par_ix.add_item(ix, par_emb)
        end_time = datetime.now()
        diff = end_time - start_time
        if diff.seconds < 5:
            time.sleep(diff.seconds)
        # Build and save the models
        model_name = f"{date.strftime('%m-%d-%Y')}.ann"
        abs_ix.build(NUM_TREES, n_jobs=-1)
        abs_ix.save(f"models/abs/a_{model_name}")
        head_ix.build(NUM_TREES, n_jobs=-1)
        head_ix.save(f"models/head/h_{model_name}")
        par_ix.build(NUM_TREES, n_jobs=-1)
        par_ix.save(f"models/par/p_{model_name}")


main_loop()

aix = AnnoyIndex(EMBED_LENGTH, "angular")
aix.load("models/head/h_01-01-2001.ann")

while True:
    sentence = input("Input a sentence: ")
    if sentence == "":
        break
    emb = get_vec(sentence)
    print(aix.get_nns_by_vector(emb, 10))
