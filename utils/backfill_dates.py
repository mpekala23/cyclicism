# I only need this file because I made stupid mistakes

import schema
from datetime import datetime
from dateutil.relativedelta import relativedelta
from pynytimes import NYTAPI
from dotenv import load_dotenv
import os
from google_images_search import GoogleImagesSearch
import random
from tqdm import tqdm
import time

load_dotenv()

API_KEY = os.getenv("NYT_KEY") or ""
GOOGLE_KEY = os.getenv("GOOGLE_KEY") or ""
nyt = NYTAPI(API_KEY, parse_dates=True)
gis = GoogleImagesSearch(GOOGLE_KEY, "a708aeeac07f04808")


START_DATE = datetime(2005, 12, 1)
END_DATE = datetime(2005, 12, 31)

dbman = schema.DBManager("meta.db")

dates = []
date = START_DATE
while date < END_DATE:
    dates.append(date)
    date += relativedelta(months=1)

for date in dates:
    print(date)
    start_time = time.time()
    data = nyt.archive_metadata(date)
    dbman.begin_transaction()
    for article in tqdm(data):
        if random.random() < 0.001:
            print("COMMITTING EARLY")
            dbman.commit_transaction()
            dbman.begin_transaction()
        web_url = article["web_url"]
        dbman.add_web_url_to_article(
            article["_id"],
            web_url,
        )
        nytimg = article["multimedia"]
        if len(nytimg) == 0:
            continue
        img_url = nytimg[0]["url"]
        dbman.add_img_url_to_article(
            article["_id"],
            img_url,
        )
    dbman.commit_transaction()
    end_time = time.time()
    seconds = end_time - start_time
    if seconds < 12:
        time.sleep(12 - seconds)
    """
    Google stuff but hit rate limit
    _search_params = {
        "q": article["headline"]["main"],
        "num": 5,
        "fileType": "jpg",
        "rights": "cc_publicdomain",
        "safe": "active",  ##
    }
    gis.search(search_params=_search_params)
    results = gis.results()
    if len(results) == 0:
        print("no img results")
        continue
    print([result.url for result in results])
    # Choose a random image from the top 5
    img = random.choice(results)
    dbman.add_img_url_to_article(
        article["_id"],
        img.url,
    )
    """
