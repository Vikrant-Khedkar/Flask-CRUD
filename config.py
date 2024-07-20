from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGODB_ATLAS_CLUSTER_URI"))
db = client[os.getenv("MONGODB_ATLAS_DATABASE_NAME")]  # Ensure "MONGODB_ATLAS_DATABASE_NAME" is a string
collection = db[os.getenv("MONGODB_ATLAS_COLLECTION_NAME")]