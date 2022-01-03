from flask import Flask, request
from utils import db

app = Flask(__name__)

@app.route("/user/<userId>", methods = ["GET"])
def user(userId):
    mydb = db.database()
    user = db.user(mydb, userId)
    print(user)
    return user