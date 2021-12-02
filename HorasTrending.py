#!/usr/bin/env python

from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_brasil = pd.read_csv("BR_youtube_trending_data.csv", parse_dates=['publishedAt', 'trending_date'])

mask = (df_brasil.view_count<=0)
df_brasil = df_brasil.loc[~mask]

df_brasil.rename(columns={'trending_date':'trendingAt'}, inplace=True)

df_brasil.insert(loc=3, column='published_date', value=df_brasil.publishedAt.dt.date)
df_brasil.insert(loc=4, column='published_month', value=df_brasil.publishedAt.dt.month_name())
df_brasil.insert(loc=5, column='published_day', value=df_brasil.publishedAt.dt.day_name())

df_brasil.insert(loc=10, column='trending_date', value=df_brasil.trendingAt.dt.date)
df_brasil.insert(loc=11, column='trending_month', value=df_brasil.trendingAt.dt.month_name())
df_brasil.insert(loc=12, column='trending_day', value=df_brasil.trendingAt.dt.day_name())

df_brasil.published_date = df_brasil.published_date.astype(np.datetime64)
df_brasil.trending_date = df_brasil.trending_date.astype(np.datetime64)

df_brasil.published_date.value_counts(normalize=True).plot.bar(figsize=(15, 8), rot=0, color='orange', ec='k')
plt.xlabel("Published Date")
plt.ylabel("Relative frequency of videos")
plt.title("Published Date by relative frequency")
plt.show()