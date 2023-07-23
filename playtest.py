from annoy import AnnoyIndex
from gen import get_vec, EMBED_LENGTH
from schema import DBManager


DB_FILE = "meta.db"
DATE = "01-2001"
AIX_FILE = f"models/abs/a_{DATE}.ann"

dbman = DBManager(DB_FILE)

aix = AnnoyIndex(EMBED_LENGTH, "angular")
aix.load(AIX_FILE)

while True:
    sentence = input("Input a sentence: ")
    if sentence == "":
        break
    emb = get_vec(sentence)
    for ix in aix.get_nns_by_vector(emb, 10):
        article = dbman.get_article_by_month_and_ix(DATE, ix)
        if article is None:
            print("WHAT! No results")
        else:
            print("------------------------------------------------")
            print(article.headline)
            print(article.lead_paragraph)
