from pymongo import MongoClient

conn = MongoClient("mongodb://localhost:27017")
db = conn["local"]  # makes a test database called "testdb"
colEdificio = db["edificio"]
colVendedor = db["vendedor"]
colLocalizacao = db["localizacao"]
