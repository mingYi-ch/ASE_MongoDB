from pymongo import MongoClient
# pprint library is used to make the output look more pretty
import pandas as pd
import numpy as np

client = MongoClient("localhost:27017")
client.drop_database('ase')
db = client.ase
data = pd.read_csv("/init_db/movies_metadata.csv", nrows = 1000)
header = data.columns.tolist()
data = data.to_numpy()

col_num = len(header)
for elem in data:
    # pprint(row.tolist())
    row = {}
    # print(elem)
    for idx in range(col_num):
        # print(elem[idx])
        val = elem[idx]
        if pd.isnull(val):
            val_ = None
        else:
            try:
                val_ = eval(val)
            except:
                val_ = val
        # print(val_)
        row[header[idx]] = val_ # parse the expression to python 
    res = db.movies.insert_one(row)
    # break
client.close()

