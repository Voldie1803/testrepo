from urllib.parse import quote_plus

username = "himeksh22218_db_user"
password = "Himi@2106"

# URL encode the username and password
encoded_username = quote_plus(username)
encoded_password = quote_plus(password)

# Construct the MongoDB URI with the encoded username and password
uri = f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.2cyjolj.mongodb.net/"

# Use the URI to connect to MongoDB
from pymongo import MongoClient
client = MongoClient(uri)

# Test connection
db = client.test
print("Connected to MongoDB")
