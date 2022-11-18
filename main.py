from pymongo.mongo_client import MongoClient
from creds import DATABSE_URL

client = MongoClient(DATABSE_URL)
print(client.test)