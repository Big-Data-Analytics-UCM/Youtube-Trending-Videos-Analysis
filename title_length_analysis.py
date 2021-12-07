import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/BR_youtube_trending_data.csv")

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


df['len_title'] = df.title.apply(len)

plt.figure(figsize=[11, 9])
plt.hist(df['len_title'], color='orange', rwidth=0.9)

median_length = df['len_title'].mean()
plt.axvline(median_length, color='#fc4f30', label='Media')

plt.legend()
plt.grid(axis='y')
plt.title('Número de apariciones según número de caracteres en el título',  fontsize=15)
plt.xlabel('Número de caracteres en el título')
plt.ylabel('Número de apariciones')

plt.show()
