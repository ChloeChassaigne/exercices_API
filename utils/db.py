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
    x = {}
    mycol = db["customers"]
    y = mycol.find()
    for x in y:
        x['_id'] = str(x['_id'])
        items.append(x)
    return {
        "Items": items,
        "Count": mycol.count_documents({})
    }

def user(db, id):
    mycol = db["customers"]
    y = mycol.find_one({"_id": ObjectId(id)})
    if y :
        y['_id'] = str(y['_id'])
        return y
    else :
        return {
            "Status": "USER_NOT_FOUND",
            "Message": "L'utilisateur demandé n'existe pas"
    }

def del_user(db, id):
    mycol = db['customers']
    mycol.delete_one({"_id": ObjectId(id)})

def limit(db):
    items = []
    mycol = db['customers']
    y = mycol.find().limit((limit))
    for data in y :
        items.append(data)
    return items


def address(db, id):
    carnet = {
        "Number": "77",
        "Street": "Chemin de la Butte",
        "City": "Toulouse",
        "PostCode": 31400
    }
    mycol = db['customers']
    y = mycol.find_one({"_id": ObjectId(id)})
    print(y)
    if y :
        y['_id'] = str(y['_id'])
        if "Address" in y :
            return y
        else : 
            profil = y.insert_one(carnet)
            return profil
    else :
        return {
            "Status": "USER_NOT_FOUND",
            "Message": "L'utilisateur n'existe pas"
    }

if "__main__" == __name__:
    mydb = database()
    #print(user(mydb, "61cae341c1a034d33b5b1ac8"))
    print(limit(mydb))