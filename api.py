from flask import Flask, render_template

app = Flask(__name__)

# NOTE: To have tailwind running while developing, run the following command in the terminal:
# npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch


@app.route("/")
def index():
    return render_template("index.html")
