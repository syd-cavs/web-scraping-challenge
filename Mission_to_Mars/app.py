from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/Mars_DB")

@app.route("/")
def home():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars_data=mars)

@app.route("/scrape")
def scrape():
    mars_info = scrape_mars.scrape()
    mongo.db.mars.update({}, mars_info, upsert=True)
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)