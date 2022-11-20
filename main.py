from pymongo.mongo_client import MongoClient
from creds import DATABSE_URL

client = MongoClient(DATABSE_URL)
database=client.get_database('sample_airbnb')
collection=database.get_collection('listingsAndReviews')
#print(collection.insert_one({'hardik':'Cool'}))
print(collection.find_one({"_id" :"10006546"}))