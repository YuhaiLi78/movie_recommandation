import nltk, re, string
from nltk.corpus import stopwords
import numpy as np
import pickle
import pandas as pd

sig_0 = np.load('polls/datasets/sig_0.npy')
sig_1 = np.load('polls/datasets/sig_0.npy')
sig = np.concatenate((sig_0, sig_1), axis=0)
data = pd.read_csv(r'polls/datasets/clean_data.csv')
indices = pd.Series(data.index, index=data['original_title'])
pivot_table = pd.read_pickle('polls/models/pivot.pkl')
with open('polls/models/knn.pkl', 'rb') as f:
    model = pickle.load(f)

def content_rec(title):
    idx=indices[title]

    model_scores = list(enumerate(list(sig[indices[idx]])))
    
    model_scores = sorted(model_scores, key=lambda x:x[1], reverse=True)
    
    model_scores = model_scores[1:11]
    
    movie_indices = [index[0] for index in model_scores]

    return data['original_title'].iloc[movie_indices]

def col_rec(title):
    idx = pivot_table[pivot_table.index.str.contains(title)]
    if idx.shape[0] == 0:
        return None

    feature = idx.iloc[0, :]
    distances, indices = model.kneighbors(feature.values.reshape(1,-1), n_neighbors=9)

    return pivot_table.iloc[indices.flatten()].index.values.tolist()[1:]

def movie_names():
    return data['original_title'].values.tolist()