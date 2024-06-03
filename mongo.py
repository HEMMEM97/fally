from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Replace the connection string with your MongoDB deployment's connection string.
client = MongoClient("mongodb+srv://lakshay:lakshaygargd@form.lsyxxi0.mongodb.net/")

# Access a database
db = client['twitter']

# Access a collection
collection = db["trending_data"]

# Insert a document
doc = {"name": "John Doe", "age": 30}
insert_result = collection.insert_one(doc)
print(f"Document inserted with _id: {insert_result.inserted_id}")

# Find a document
find_result = collection.find_one({"name": "John Doe"})
print(f"Found document: {find_result}")

# Update a document
update_result = collection.update_one({"name": "John Doe"}, {"$set": {"age": 31}})
print(f"Documents updated: {update_result.modified_count}")

# Delete a document
delete_result = collection.delete_one({"name": "John Do"})
print(f"Documents deleted: {delete_result.deleted_count}")