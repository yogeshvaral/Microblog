from flask import Flask, render_template,request,jsonify
# from mongo_client import mongo_client
from pymongo import MongoClient
import datetime

def create_app():
    app = Flask(__name__)

    mongo_client = MongoClient("mongodb://localhost:27017")
    blog = mongo_client.microblog
    entries_collection = blog.entries


    @app.route("/",methods=['GET','POST'])
    def home():
        if request.method == 'POST':
            entry_content = request.form.get('content')
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
            result = entries_collection.insert_one({'content':entry_content,'date':formatted_date})

        entries_with_date  = [
            (
                entry['content'],
                entry['date'],
                datetime.datetime.strptime(entry['date'], "%Y-%m-%d").strftime("%b %d")
            )
            for entry in entries_collection.find({})
        ]    
        return render_template("home.html",entries=entries_with_date)
    
    return app