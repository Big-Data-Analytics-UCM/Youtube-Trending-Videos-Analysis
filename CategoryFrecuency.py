from datetime import datetime
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



with open('BR_category_id.json') as json_file:
    data = json.load(json_file)
    store_list = dict()
    for item in data['items']:
        index = int(item['id'])
        store_list[index] = item['snippet']['title']




df_brasil = pd.read_csv("BR_youtube_trending_data.csv", parse_dates=['publishedAt', 'trending_date'])


df_brasil = df_brasil.replace({"categoryId": store_list})

mask = (df_brasil.view_count<=0)
df_brasil = df_brasil.loc[~mask]

df_brasil.categoryId.value_counts(normalize=True)
df_brasil.categoryId.value_counts(normalize=True).plot.bar(figsize=(15, 8), rot=0, color='orange', ec='k')
plt.xlabel("Videos Category ID")
plt.ylabel("Relative frequency of videos")
plt.title("Video categories by relative frequency")
plt.show()