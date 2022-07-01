import pymongo 
import os

DB_NAME = os.environ.get("DB_NAME","")
DB_URL = os.environ.get("DB_URL","")
mongo = pymongo.MongoClient(DB_URL)
db = mongo[DB_NAME]
dbcol = db["user"]

def insert(chat_id):
            user_id = int(chat_id)
            user_det = {"_id":user_id,"file_id":None , "date":0}
            try:
                        dbcol.insert_one(user_det)
            except:
                        return 'new'

def addthumb(chat_id, file_id):
	dbcol.update_one({"_id":chat_id},{"$set":{"file_id":file_id}})
	
def delthumb(chat_id):
	dbcol.update_one({"_id":chat_id},{"$set":{"file_id":None}})
	
def find(chat_id):
            id =  {"_id":chat_id}
            x = dbcol.find(id)
            for i in x:
                        return i["file_id"] 

def getid():
            return [key["_id"] for key in dbcol.find()]
    
def find_one(id):
	return dbcol.find_one({"_id":id})
