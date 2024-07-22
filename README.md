# zomato_analysis

# Zomato Data Analysis

This repository contains code for analyzing Zomato data. The analysis includes reading data from a SQLite database, handling missing values, performing text analysis, and generating geographical visualizations.

## Prerequisites

Before running the code, ensure you have the following libraries installed:

- pandas
- sqlite3
- numpy
- matplotlib
- seaborn
- nltk
- geopy
- folium

You can install these libraries using pip:

```bash
pip install pandas sqlite3 numpy matplotlib seaborn nltk geopy folium
```

## Script Overview

### The script performs the following tasks:

1. Importing Libraries: Importing necessary Python libraries.
2. Reading Data from Database: Connecting to SQLite database and reading data into a DataFrame.
3. Handling Missing Values: Checking for and handling missing values in the data.
4. Analyzing Relation Between Online Order and Rating: Analyzing the relationship between online orders and ratings.
5. Text Analysis: Performing text analysis on restaurant reviews.
6. Frequency Distribution: Analyzing the frequency distribution of words in reviews.
7. Bigram and Trigram Analysis: Analyzing bigrams and trigrams in reviews.
8. Geographical Coordinates from Data: Fetching geographical coordinates for restaurant locations.
9. Spatial Analysis: Creating heatmaps to visualize restaurant data geographically.

## How to Run

1. Ensure you have the required libraries installed.
2. Place the SQLite database file (zomato_rawdata.sqlite) in the same directory as the script.

3. Run the script using Python:

```
python zomato_data_analysis.py
```

4. The script will generate heatmaps and other visualizations which will be saved in the current directory.

## Conclusion

This script performs comprehensive data analysis on Zomato data, covering missing values, text analysis, frequency distribution, and geographical visualization. The heatmaps provide a visual representation of the concentration of different types of restaurants across Bangalore.

1. Relation Between Online Order and Rating:
2. Unigram, Bigram and Trigram Analysis:
3. Spatial Analysis(HeatMap):
