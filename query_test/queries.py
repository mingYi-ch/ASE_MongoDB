from pymongo import MongoClient

client = MongoClient("localhost:27017")
movies = client.ase.movies

doc = movies.find_one({'adult': False})
assert(doc['adult'] == False)
