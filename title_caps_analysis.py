import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("BR_youtube_trending_data.csv")

mask = (df.view_count <= 0)
df = df.loc[~mask]

df.drop(['channelId', 'tags', 'thumbnail_link', 'comments_disabled', 'ratings_disabled', 'description'], axis=1,
        inplace=True)

def caps_percent(title):
    if len(title) <= 0:
        return 0
    s = 0
    for cr in title:
        if cr.isupper():
            s += 1
    return ((round((s/len(title))*100, 0)) // 5)*5  # Clasificar de 5 en 5


df['percent_caps'] = df.title.apply(caps_percent)

plt.figure(figsize=[11, 9])
plt.hist(df['percent_caps'], color='orange', rwidth=0.9)

median_caps = df['percent_caps'].mean()
plt.axvline(median_caps, color='#fc4f30', label='Media')

plt.legend()
plt.grid(axis='y')
plt.title('Número de apariciones según porcentaje de mayúsculas en el título',  fontsize=15)
plt.xlabel('Porcentaje de mayúsculas en el título')
plt.ylabel('Número de apariciones')

plt.show()
