import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from warnings import filterwarnings
filterwarnings('ignore')


# read data from database
con = sqlite3.connect('zomato_rawdata.sqlite')

df = pd.read_sql_query('SELECT * FROM Users',con)
print(df.head(2))
print(df.shape)
print(df.columns)

# missing values

print(df.isnull().sum())

print(df['rate'].unique())

df['rate']=df['rate'].replace(('NEW','-'),np.nan)
print(df['rate'].unique())

df['rate'] = df['rate'].apply(lambda x : float(x.split('/')[0]) if type(x)== str else x)
print(df['rate'])

# relation between online order and rating

x = pd.crosstab(df['rate'],df['online_order'])
print(x)

x.plot(kind='bar',stacked=True)
plt.show()

print(x.sum(axis=1).astype(float))

normalized_df = x.div(x.sum(axis=1).astype(float),axis=0)
print(normalized_df*100)
(normalized_df*100).plot(kind='bar' ,stacked = True)
plt.show()

# Text Analysis
print(df['rest_type'].isnull().sum())

data = df.dropna(subset=['rest_type'])
print(data['rest_type'].isnull().sum())

print(data['rest_type'].unique())

quick_bites_df = data[data['rest_type'].str.contains('Quick Bites')]

print(quick_bites_df.shape)

print(quick_bites_df.columns)

quick_bites_df['reviews_list']= quick_bites_df['reviews_list'].apply(lambda x : x.lower())

from nltk.corpus import RegexpTokenizer

tokenizer = RegexpTokenizer('[a-zA-Z]+')
print(tokenizer)

sample = data[0:10000]

reviews_token = sample['reviews_list'].apply(tokenizer.tokenize)
print(reviews_token)

# uigram analysis

from nltk.corpus import stopwords

stop = stopwords.words('english')
print(stop)

stop.extend(['Rated', 'RATED', 'rated', 'n', 'nan','x'])
print(stop)

rev3 = reviews_token[3]

print([token for token in rev3 if token not in stop])

reviews_token_clean = reviews_token.apply(lambda each_review : [token for token in each_review if token not in stop])
print(reviews_token_clean)

print(type(reviews_token_clean))

total_reviews_2D = list(reviews_token_clean)
total_reviews_1D = []

for review in total_reviews_2D:
    for word in review:
        total_reviews_1D.append(word)

print(total_reviews_1D)

from nltk import FreqDist

fd = FreqDist()

for word in total_reviews_1D:
    fd[word] = fd[word]+1

print(fd.most_common(20))

fd.plot(20)
plt.show()

# Bigram and Tigram analysis

from nltk import bigrams, trigrams

bi_grams = bigrams(total_reviews_1D)
fd_bi_grams = FreqDist()
for bigram in bi_grams:
    fd_bi_grams[bigram] = fd_bi_grams[bigram]+1

print(fd_bi_grams.most_common(20))
fd_bi_grams.plot(20)
plt.show()

tri_grams = trigrams(total_reviews_1D)
fd_tri_grams = FreqDist()
for trigram in tri_grams:
    fd_tri_grams[trigram] = fd_tri_grams[trigram]+1

print(fd_tri_grams.most_common(20))
fd_tri_grams.plot(20)
plt.show()

# Geographical coordinates from data

print(df['location'])

print(df['location'].unique())
print(len(df['location'].unique()))

df['location'] = df['location'] + " ,Bangalore , Karnataka , India"
print(df['location'])
print(df['location'].unique())

df_copy = df.copy()

print(df_copy['location'].isnull().sum())

df_copy=df_copy.dropna(subset=['location'])

print(df_copy['location'].isnull().sum())
print(df_copy['location'].unique())

locations = pd.DataFrame(df_copy['location'].unique())
locations.columns = ['name']
print(locations)

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='app',timeout=None)

lat = []
lon = []

for location in locations['name']:
        location = geolocator.geocode(location)
        if location is None:
             lat.append(np.nan)
             lon.append(np.nan)
        else:
             lat.append(location.latitude)
             lon.append(location.longitude)

locations['latitude'] = lat
locations['longitude'] = lon
print(locations)

# Spatial Analysis

print(locations.isnull().sum())
print(locations[locations['latitude'].isna()])

locations['latitude'][79] = 13.0163
locations['longitude'][79] = 77.6785

locations['latitude'][85] = 13.0068
locations['longitude'][85] = 77.5813

print(df['cuisines'].isnull().sum())
df = df.dropna(subset=['cuisines'])

north_india = df[df['cuisines'].str.contains('North Indian')]
print(north_india.shape)

print(north_india['location'].value_counts())

north_india_rest_count = north_india['location'].value_counts().reset_index().rename(columns={'location':'name','count':'count' })

print(north_india_rest_count)

heatmap_df = north_india_rest_count.merge(locations, on='name', how='left')

print(heatmap_df)

import folium
basemap = folium.Map()

from folium.plugins import HeatMap

HeatMap(heatmap_df[['latitude','longitude','count']]).add_to(basemap)
map_file = 'heatmap_df'
map_file.save("basemap.html")

def get_heatmap(cuisine):
     cuisine_df = df[df['cuisines'].str.contains(cuisine)]
     cuisine_rest_count = cuisine_df['location'].value_counts().reset_index().rename(columns={'location':'name','count':'count' })
     heatmap_df = cuisine_rest_count.merge(locations, on='name', how='left')
     print(heatmap_df.head(4))

     basemap = folium.Map()
     HeatMap(heatmap_df[['latitude','longitude','count']]).add_to(basemap)
     return basemap

heatmap = get_heatmap('South Indian')

heatmap.save("heatmap.html")

print(df['cuisines'].unique())