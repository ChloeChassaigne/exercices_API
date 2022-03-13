import pymongo
from bson.objectid import ObjectId 

#Connection database
def database():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["database"]
    return mydb
#Add data
def add_data(db, data):
    mycol = db["customers"]
    x = mycol.insert_one(data)
    return x.inserted_id
#Find all users and how many users
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
#Find a user with an Id
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
#Delete user with an Id
def del_user(db, id):
    mycol = db['customers']
    mycol.delete_one({"_id": ObjectId(id)})
#Limit to show users
def limit(db, limit):
    items = []
    x = {}
    mycol = db["customers"]
    y = mycol.find().limit(limit)
    for x in y:
        x['_id'] = str(x['_id'])
        items.append(x)
    return {
        "Items": items,
        "Count": len(items)
    }
#Add an address a specific user (Id)
def address(db, id):
    mycol = db['customers']
    y = mycol.find_one({"_id": ObjectId(id)})
    print(y)
    if y :
        y['_id'] = str(y['_id'])
        if "Address" in y :
            return y
        else : 
            return None
    else :
        return {
            "Status": "USER_NOT_FOUND",
            "Message": "L'utilisateur demandé n'existe pas"
    }
#Add an address a specifi user (Id)
def put_address(db, id, update):
    mycol = db['customers']
    myquery = { "_id": ObjectId(id)}
    newvalues = {"$set": {"Address": update}}
    if myquery :
        return mycol.update_one(myquery, newvalues)
    else :
        return {
            "Status": "USER_NOT_FOUND",
            "Message": "L'utilisateur n'existe pas"
    }
    
#if "__main__" == __name__:
    #mydb = database()
    #print(user(mydb, "61cae341c1a034d33b5b1ac8"))
    #print(limit(mydb))