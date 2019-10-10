import numpy as np 
import pandas as pd 


def getdata():
    ratings = pd.read_csv("/Projects/movielens/data/ratings.csv").rename(columns={'userId':'user', 'movieId':'movie'})
    print(ratings.head())
    urm = ratings[['user', 'movie', 'rating']]
    
    return urm
