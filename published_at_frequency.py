#!/usr/bin/env python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# countries = ["BR", "CA", "DE", "FR", "GB", "IN", "JP", "KR", "MX", "RU", "US"]

def published_at_frequency(country):
    ruta = 'data/' + country + '_youtube_trending_data.csv'
    df = pd.read_csv(ruta, parse_dates=['publishedAt', 'trending_date'])

    mask = (df.view_count <= 0)
    df = df.loc[~mask]

    df.rename(columns={'trending_date': 'trendingAt'}, inplace=True)

    df.insert(loc=3, column='published_date', value=df.publishedAt.dt.date)
    df.insert(loc=4, column='published_month', value=df.publishedAt.dt.month_name())
    df.insert(loc=5, column='published_day', value=df.publishedAt.dt.day_name())

    df.insert(loc=10, column='trending_date', value=df.trendingAt.dt.date)
    df.insert(loc=11, column='trending_month', value=df.trendingAt.dt.month_name())
    df.insert(loc=12, column='trending_day', value=df.trendingAt.dt.day_name())

    df.published_date = df.published_date.astype(np.datetime64)
    df.trending_date = df.trending_date.astype(np.datetime64)

    # Agrupar por franjas

    df.published_date.value_counts(normalize=True).plot.bar(figsize=[15, 8], rot=0, color='orange', ec='k')
    plt.xlabel("Published Date")
    plt.ylabel("Relative frequency of videos")
    plt.title("Published Date by relative frequency")
    plt.savefig("published_at_frequency_" + country + ".png", dpi=100)
