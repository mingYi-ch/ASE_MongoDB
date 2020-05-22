import pandas as pd
import numpy as np

def preprocess_data(meta_path, rating_path, movie_num = 40000, testrows = None):
    # find 5000 movies with top popularity
    cols = ['id', 'genres', 'budget','imdb_id', 'popularity', 'poster_path', 'release_date', 'revenue', 'runtime', 'title'] # add rating
    meta = pd.read_csv(meta_path, usecols=cols, nrows = testrows).astype({'budget': 'str', 'revenue': 'str'})
    # print(meta.index)
    # remove rows where id is date, or budget and revenue is 0, id is not number
    ridx_bad =[idx for idx, val in meta['budget'].items() if val < '1' or '/' in val]\
                + [idx for idx, val in meta['revenue'].items() if val < '1' or '/' in val] \
                + [idx for idx, val in meta['id'].items() if not isinstance(val, int) and not val.isdigit()]
    meta.drop(labels = np.unique(ridx_bad), inplace = True)

    # sort by popularity
    meta.dropna().astype({'popularity': np.float}) \
        .sort_values(by = 'popularity', inplace = True, ascending = False)
    #meta_selected = meta.drop(np.arange(movie_num, meta.shape[0]))

    # print(meta_selected['title'])  dtype={'movieId': np.int}
    cols_r = ['movieId', 'rating']
    rating = pd.read_csv("./ratings.csv", usecols=cols_r, nrows= testrows)
    avg_rating = rating.groupby(by = 'movieId', as_index = False).mean().round({'rating': 1})
    # avg_rating.to_csv('rating.csv')
    
    # join the two dataframes
    meta['id'] = meta['id'].astype(int)
    avg_rating['movieId'] = avg_rating['movieId'].astype(int)
    df_new = meta.merge(avg_rating, left_on = 'id', right_on = 'movieId', how = 'inner').round({'popularity': 2}).sample(frac = 1)
    # only keep the year number in release date
    df_new['release_date'] = [val[:4] for idx, val in df_new['release_date'].items()]
    # print([idx for idx, val in df_new['release_date'].items() if len(val) < 4])
    df_new.to_csv('movie_data.csv', index = False)

if __name__ == '__main__':
    meta_path = "./movies_metadata.csv"
    rating_path = "./ratings.csv"
    preprocess_data(meta_path, rating_path)
