from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_mars import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection

mongo = PyMongo(app, uri="mongodb://localhost:27017/mission_to_mars_app")

@app.route("/")
def index():
    scrape = mongo.db.scrapes.find_one()
    return render_template("index.html", scrape=scrape)


@app.route("/scrape")
def scraper():
    scrapes = mongo.db.scrapes
    scrape_data = scrape_mars()
    scrapes.update({}, scrape_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
