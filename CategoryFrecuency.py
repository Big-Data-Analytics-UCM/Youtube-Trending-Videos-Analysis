#!/usr/bin/env python

from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_brasil = pd.read_csv("BR_youtube_trending_data.csv", parse_dates=['publishedAt', 'trending_date'])

mask = (df_brasil.view_count<=0)
df_brasil = df_brasil.loc[~mask]

df_brasil.categoryId.value_counts(normalize=True)
df_brasil.categoryId.value_counts(normalize=True).plot.bar(figsize=(15, 8), rot=0, color='orange', ec='k')
plt.xlabel("Videos Category ID")
plt.ylabel("Relative frequency of videos")
plt.title("Video categories by relative frequency")
plt.show()
