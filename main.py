from flask import Flask, request
from utils import db

app = Flask(__name__)

@app.route("/user/<userId>", methods = ["GET"])
def user(id):
    mydb = db.database()
    user = db.user(mydb, id)
    if user :
        return user
    else :
        return {
        "Status": "USER_NOT_FOUND",
        "Message": "L'utilisateur demandé n'existe pas"
    }