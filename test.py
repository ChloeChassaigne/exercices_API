from flask import Flask, request
from utils import db

app = Flask(__name__)
#Route "/" return a message
@app.route("/")
def hello():
    return {
        "msg": "Hello World"
    }
#Route "/hello" return message with a user name
@app.route("/hello", methods=["GET"])
def get_username():
    name = request.args.get("name")
    return {
        "msg": f"Hello {name}"
    }
#Add new user
@app.route("/new", methods=["POST"])
def post_data():
    if 'FirstName' in request.get_json() and 'LastName' in request.get_json():
        mydb = db.database()
        data = {
                "FirstName": f"{request.get_json()['FirstName']}", 
                "LastName": f"{request.get_json()['LastName']}"
            }
        
        id = db.add_data(mydb, data)
        print(type(id))
        return {
            "id": str(id)
        }
    else:
        return {
            "error": "MISSING_ELEMENTS",
            "message": "Body must contain FirstName and LastName"
        }
#Show all users
@app.route('/all', methods=['GET'])
def find_data():
    mydb = db.database()
    items = db.find_all(mydb)
    return items
#Show user with a specific Id
@app.route('/user/<id>', methods=['GET'])
def user(id):
    mydb = db.database()
    user = db.user(mydb, id)
    return user