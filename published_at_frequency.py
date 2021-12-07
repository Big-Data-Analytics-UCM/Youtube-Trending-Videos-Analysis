#!/usr/bin/env python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# countries = ["BR", "CA", "DE", "FR", "GB", "IN", "JP", "KR", "MX", "RU", "US"]

def published_at_frequency(country):
    ruta = 'data/' + country + '_youtube_trending_data.csv'
    df = pd.read_csv(ruta, parse_dates=['publishedAt', 'trending_date'], engine='python', error_bad_lines=False)

    mask = (df.view_count <= 0)
    df = df.loc[~mask]

    df.rename(columns={'trending_date': 'trendingAt'}, inplace=True)

    df.insert(loc=3, column='published_hour', value=df.publishedAt.dt.hour)

    df.published_hour.value_counts(normalize=True).plot.bar(figsize=[15, 8], rot=0, color='orange', ec='k')
    plt.xlabel("Published Date")
    plt.ylabel("Relative frequency of videos")
    plt.title("Published Date by relative frequency")
    plt.savefig("published_at_frequency_" + country + ".png", dpi=100)


published_at_frequency("BR")