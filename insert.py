from pymongo import MongoClient

# Connect to the MongoDB Atlas cluster
client = MongoClient("mongodb+srv://himeksh22218_db_user:Himi%402106@cluster0.2cyjolj.mongodb.net/")

# Create a database (it will be created when you insert data)
db = client["myDatabase"]  # This will create 'myDatabase' if it doesn't exist

# Create a collection within the database
collection = db["myCollection"]  # This will create 'myCollection' if it doesn't exist

# Insert a document into the collection
collection.insert_one({"name": "John", "age": 30})

print("Database and collection created with data.")
