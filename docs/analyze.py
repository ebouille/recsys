import numpy as np 
import pandas as pd 

pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 500)


links = pd.read_csv("/Projects/movielens/data/links.csv")
print("--links--")
print(links.head())

movies = pd.read_csv("/Projects/movielens/data/movies.csv")
print("\n\n--movies--")
print(movies.head())

ratings = pd.read_csv("/Projects/movielens/data/ratings.csv")
print("\n\n--ratings--")
print(ratings.head())

tags = pd.read_csv("/Projects/movielens/data/tags.csv")
print("\n\n--tags--")
print(tags.head())
print('number of different tags: ', tags['tag'].nunique())
print('number of movies with tags: ', tags['userId'].nunique())


movies_tags = pd.merge(movies, tags, on='movieId', how='left')
print("\n\n--movies and tags--")
print(movies_tags.head())







# movies_tags.fillna("", inplace=True)
# mixed = pd.DataFrame(movies_tags.groupby('movieId')['tag'].apply(
#                              lambda x: "%s" % ' '.join(x)))
# df = pd.merge(movies, mixed, on='movieId', how='left')
# df ['metadata'] = df[['tag', 'genres']].apply(
#                              lambda x: ' '.join(x), axis = 1)
# df[['movieId','title','metadata']].head(3)

# print(df.head())

