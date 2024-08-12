from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)


client= MongoClient('mongodb://localhost:27017/')
db=client['resume']
collection=db['details']


@app.route('/', methods=['GET'])
def index():
   
    return render_template('index.html')



