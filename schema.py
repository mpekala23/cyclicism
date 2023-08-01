import sqlite3
from typing import NamedTuple, Union


class Article(NamedTuple):
    """
    A class representing the information about an article that
    we want to persist and recall (after getting the annoy ix)
    """

    id: str
    month: str
    annoy_ix: int
    abstract: str
    headline: str
    lead_paragraph: str
    img_url: Union[str, None]
    web_url: str


class DBManager:
    """
    Simple class for holding a connection to the local sqlite
    """

    def __init__(self, db_fname: str):
        self.con = sqlite3.connect(db_fname)
        self.cur = self.con.cursor()
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS article (
                    id text,
                    month text,
                    annoy_ix integer,
                    abstract text,
                    headline text,
                    lead_paragraph text
            );
            """
        )
        self.con.commit()

    def begin_transaction(self):
        self.cur.execute("BEGIN TRANSACTION;")

    def commit_transaction(self):
        self.con.commit()

    def add_article(self, article: Article, commit=False):
        """
        Adds an articles metadata to the database
        """
        sql = f"""
            INSERT INTO article VALUES (
            ?,
            ?,
            {article.annoy_ix},
            ?,
            ?,
            ?,
            ?,
            ?,
            );
            """
        self.cur.execute(
            sql,
            [
                article.id,
                article.month,
                article.abstract,
                article.headline,
                article.lead_paragraph,
                article.img_url,
                article.web_url,
            ],
        )
        if commit:
            self.con.commit()

    def get_article_by_month_and_ix(self, month: str, ix: int) -> Union[Article, None]:
        """
        Fetch an article using month string and annoy ix
        """
        res = self.cur.execute(
            f"""
            SELECT * FROM article WHERE month='{month}' AND annoy_ix='{ix}';
            """
        )
        raw = res.fetchone()
        if not raw:
            # Maybe this should throw an error?
            return None
        return Article(
            id=raw[0],
            month=raw[1],
            annoy_ix=raw[2],
            abstract=raw[3],
            headline=raw[4],
            lead_paragraph=raw[5],
            img_url=raw[6] or None,
            web_url=raw[7],
        )

    def add_web_url_to_article(self, id: str, web_url: str):
        """
        Add a web url to an article
        """
        self.cur.execute(
            f"""
            UPDATE article SET web_url='{web_url}' WHERE id='{id}';
            """
        )
        self.con.commit()

    def add_img_url_to_article(self, id: str, img_url: str):
        """
        Add an image url to an article
        """
        self.cur.execute(
            f"""
            UPDATE article SET img_url='{img_url}' WHERE id='{id}';
            """
        )
        self.con.commit()
