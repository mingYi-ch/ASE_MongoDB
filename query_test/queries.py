from pymongo import MongoClient

client = MongoClient("localhost:27017")
movies = client.ase.movies 

# find 20 movies at one time, and return two each time to the client,return only fields we want
docs_num = movies.find().count()
assert(docs_num > 1000)
doc = movies.find().limit(1)
print(list(doc))
# print(list(docs))
# aggregated, features for ratings


