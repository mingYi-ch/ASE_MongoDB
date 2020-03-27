from pymongo import MongoClient
import json

client = MongoClient("localhost:27017")
moives = client.ase.moives

fivestar = moives.find_one({'adult': False})
print(fivestar)
