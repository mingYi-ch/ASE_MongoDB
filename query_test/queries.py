from pymongo import MongoClient

client = MongoClient("localhost:27017")
movies = client.ase.movies 

# find 20 movies at one time, and return two each time to the client,return only fields we want
docs = movies.find({'id': 1, 'revenue': 1, 'runtime': 1, 'popularity': 1}).limit(20)
assert(len(list(docs)) > 0)

# aggregated, features for ratings


