import pymongo
from bson.objectid import ObjectId 

def database():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["database"]
    return mydb

def add_data(db, data):
    mycol = db["customers"]
    x = mycol.insert_one(data)
    return x.inserted_id

def find_all(db):
    items = []
    mycol = db["customers"]
    for x in mycol.find():
        print(x)
        items.append({
            "id": str(x["_id"]),
            "FirstName": x["FirstName"],
            "LastName": x["LastName"]
        })
    return {
        "Items": items,
        "Count": mycol.count_documents({})
    }

def user(db, id):
    mycol = db["customers"]
    y = mycol.find_one({"_id": ObjectId(id)})
    return {
            "id": str(y["_id"]),
            "FirstName": y["FirstName"],
            "LastName": y["LastName"],
            "Adress" : {
                "Number": y["Number"],
                "Street": y["Street"],
                "City": y["City"],
                "PostCode": y["PostCode"]
            }
    }

if "__main__" == __name__:
    mydb = database()
    user(mydb, "61cae341c1a034d33b5b1ac8")