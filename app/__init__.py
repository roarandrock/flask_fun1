from flask import Flask
from flask_pymongo import PyMongo
from app import secrets_mine

app = Flask(__name__)
app.config["DEBUG"] = True
db_username, db_pass = secrets_mine.login_details()
# app.config["MONGO_URI"] = "mongodb+srv://ReadWriter1:MvnmPUNcpElMGKMd@clustertestgame-zbbya.gcp.mongodb.net/test?retryWrites=true&w=majority"
# uri1 = "mongodb+srv://ReadWriter1:MvnmPUNcpElMGKMd@clustertestgame-zbbya.gcp.mongodb.net/gettingStarted" # points directly to db
uri1 = "mongodb+srv://" + db_username + ":" + db_pass + "@clustertestgame-zbbya.gcp.mongodb.net/gettingStarted"
mongo = PyMongo(app, uri=uri1, maxPoolSize=50, connect=False)

# gettingStarted is the DB, team is the collection,

from app import routes, models

# how to start:
# set FLASK_APP=demo.py
# flask run
# handy: set FLASK_ENV=development