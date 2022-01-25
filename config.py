from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.config['SECRET_KEY'] = '0192023a7bbd73250516f069df18b500'
app.config['TEMPLATES_AUTO_RELOAD'] = True

url = "mongodb+srv://admin123:Admin_123@cluster1.qli83.mongodb.net/webshop_db?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.webshop_db
