from flask import Flask
import random
from pymongo import MongoClient
import tools.mongotools as mongo
import tools.sqltools as sql
import tools.gen_tools as tools
import json
import pymysql
import sqlalchemy as alch
from flask import Flask, request, jsonify

#mongo.all_sentences()

app = Flask(__name__)

@app.route("/")
def greeting ():
    manual="""This is the manual to use my web API <br>
    <br>
    The API provides access to historical headlines and their sentiment
    as well as to the current news via the news API.<br>
    <br>
    In order to get the historical news use the following format:<br>
    - domain/news/[date]<br>
    - replace date with your desired data in format YYYY-MM-DD<br>
    <br>
    <br>
    In order to get current news use the endpoint:<br>
    - domain/cur_news/[source]/[date]<br>
    - example source: business-insider, bbc-news, the-washington-times, time<br>
    - complete list of sources is here: https://newsapi.org/docs/endpoints/sources"""
    return manual

# GET

@app.route("/line/<name>")
def all_from_mongo(name):
    return jsonify(mongo.all_sentences(name))

@app.route("/news/<date>")
def all_from_sql(date):
    return jsonify(sql.get_news(date))

@app.route("/cur_news/<source>/<date>")
def get_news(source, date):
    return tools.cur_news(source,date)

"""
## POST
@app.route("/newline", methods=["POST"])
def insert_message():

    database = request.args["db"]

    if database == "mongo":
        dict_ = {"scene": request.form.get("scene"),
            "character_name": request.form.get("character_name"), 
            "dialogue": request.form.get("dialogue")}
        return mongo.inserting(dict_)


    elif database == "sql":
        scene = request.form.get("scene")
        char_ = request.form.get("char_")
        dialogue = request.form.get("dialogue")
        return sql.new_message(scene, char_, dialogue)

    else:
        return "You need to include the db param: either mongo or sql"


app.run(debug=True)
"""    

if __name__ == '__main__':
    app.run(debug=True)














