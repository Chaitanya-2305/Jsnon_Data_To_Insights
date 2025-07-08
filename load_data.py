import json
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["dashboard_db"]
collection = db["insights"]

# Optional: clear old data
collection.delete_many({})

try:
    with open("jsondata.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        if isinstance(data, list):
            collection.insert_many(data)
        else:
            collection.insert_one(data)
        print(f"✅ Inserted {collection.count_documents({})} documents into MongoDB.")
except FileNotFoundError:
    print("❌ jsondata.json file not found.")
except Exception as e:
    print("❌ Error loading data:", e)
