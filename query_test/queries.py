from pymongo import MongoClient

client = MongoClient("localhost:27017")
moives = client.ase.moives

doc = moives.find_one({'adult': False})
assert(doc['adult'] == False)
    
