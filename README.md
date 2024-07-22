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
<img width="616" alt="Screen Shot 2024-07-22 at 15 52 37" src="https://github.com/user-attachments/assets/3ea48a73-d05a-4044-8b6a-5c6f351d158c">
<img width="613" alt="Screen Shot 2024-07-22 at 15 52 50" src="https://github.com/user-attachments/assets/0c61b75b-652f-44fd-bfad-9ba573c1ce73">

2. Unigram, Bigram and Trigram Analysis:
<img width="1357" alt="Screen Shot 2024-07-22 at 16 03 34" src="https://github.com/user-attachments/assets/f057ca12-2752-425f-8a0c-18b18472a10c">
<img width="1333" alt="Screen Shot 2024-07-22 at 16 04 27" src="https://github.com/user-attachments/assets/1c4bd9cd-94e6-4276-a0f7-fd9e910d6e35">
<img width="1291" alt="Screen Shot 2024-07-22 at 16 05 18" src="https://github.com/user-attachments/assets/7082d69c-c76a-4cd0-b44d-e77eec08e94f">

3. Spatial Analysis(HeatMap):
<img width="1276" alt="Screen Shot 2024-07-18 at 13 45 19" src="https://github.com/user-attachments/assets/d5f963f2-9042-44b8-aca8-364817b34b03">
