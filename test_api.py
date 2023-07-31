# THIS IS AN AUTO-GENERATED FILE. DO NOT EDIT
from flask import Flask, render_template
from typing import Union, NamedTuple

app = Flask(__name__)


class FrontendArticle(NamedTuple):
    title: str
    abstract: str
    img_url: Union[str, None]
    article_url: str
    date_str: str


results = [
    (
        FrontendArticle(
            title="The title",
            abstract="The abstract",
            img_url="https://upload.wikimedia.org/wikipedia/commons/b/bd/Test.svg",
            article_url="https://www.nytimes.com/2021/05/02/us/politics/biden-100-days.html",
            date_str="April 1st, 2004"
        ),
        FrontendArticle(
            title="The title",
            abstract="The abstract",
            img_url="https://upload.wikimedia.org/wikipedia/commons/b/bd/Test.svg",
            article_url="https://www.nytimes.com/2021/05/02/us/politics/biden-100-days.html",
            date_str="May 10th, 2023"
        )
    ),
]

@app.route("/")
def index():
    return render_template("index.html", results=results * 10)
