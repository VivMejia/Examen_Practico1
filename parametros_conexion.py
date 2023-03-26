import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['Examen_Practico_1']
collection = db['Productos']