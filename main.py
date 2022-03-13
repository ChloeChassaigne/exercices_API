from crypt import methods
from flask import Flask, request
from utils import db

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def find_data():
    mydb = db.database()
    limit = request.args.get('limit')
    if limit == None :
        items = db.find_all(mydb)
    else :
        items = db.limit(mydb, int(limit))
    return items

@app.route("/user/<userId>", methods = ["GET"])
def user(userId):
    mydb = db.database()
    user = db.user(mydb, userId)
    print(user)
    return user

@app.route("/users", methods=["POST"])
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

@app.route("/user/<userId>", methods = ["DELETE"])
def del_user(userId):
    mydb = db.database()
    del_user = db.del_user(mydb, userId)
    return {}

@app.route("/user/<userId>/address", methods = ["GET"])
def address(userId):
    mydb = db.database()
    address = db.user(mydb, userId)
    print(address)
    return address

@app.route("/user/address/<userId>", methods= ["PUT"])
def put_address(userId):
    mydb = db.database()
    db.put_address(mydb, userId, request.get_json())
    return {}