from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/Mars_DB")
db = mongo.db

@app.route("/")
def home():
    mars = mongo.db.mars.find_one()
    app.logger.info(mars)
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.scrape()
    app.logger.info(mars_data)
    db.mars_data.update({}, mars_data, upsert=True)
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)