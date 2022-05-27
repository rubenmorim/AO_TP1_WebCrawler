from pymongo import MongoClient

conn = MongoClient("mongodb://localhost:27017")
db = conn["local"]  # makes a test database called "testdb"
col = db["edificio"]

