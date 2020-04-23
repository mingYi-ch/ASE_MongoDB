import pandas as pd
import numpy as np

def preprocess_data(meta_path, rating_path, movie_num = 40000, testrows = None):
    # find 5000 movies with top popularity
    cols = ['id', 'genres', 'budget', 'popularity', 'poster_path', 'release_date', 'revenue', 'runtime', 'title'] # add rating
    meta = pd.read_csv(meta_path, usecols=cols, nrows = testrows).astype({'budget': 'str', 'revenue': 'str'})
    # print(meta.index)
    # remove rows where id is date, or budget and revenue is 0
    ridx_bad =[idx for idx, val in meta['budget'].items() if val < '1' or '/' in val]\
                + [idx for idx, val in meta['revenue'].items() if val < '1' or '/' in val]
    # print(ridx_bad)
    print(meta.loc[ridx_bad])
    meta.drop(labels = np.unique(ridx_bad), inplace = True)

    # sort by popularity
    meta.dropna().astype({'popularity': np.float, 'id': 'str'}) \
        .sort_values(by = 'popularity', inplace = True, ascending = False)
    #meta_selected = meta.drop(np.arange(movie_num, meta.shape[0]))
    # meta_selected = meta

    # print(meta_selected['title'])
    cols_r = ['movieId', 'rating']
    rating = pd.read_csv("./ratings.csv", usecols=cols_r, dtype={'movieId': 'str'}, nrows= testrows)
    avg_rating = rating.groupby(by = 'movieId', as_index = False).mean().round({'rating': 1})
    avg_rating.to_csv('rating.csv')
    
    # join the two dataframes
    df_new = meta.merge(avg_rating, left_on = 'id', right_on = 'movieId', how = 'inner').round({'popularity': 2}).sample(frac = 1)
    # print(df_new)
    df_new.to_csv('movie_data.csv', index = False)

if __name__ == '__main__':
    meta_path = "./movies_metadata.csv"
    rating_path = "./ratings.csv"
    preprocess_data(meta_path, rating_path)
