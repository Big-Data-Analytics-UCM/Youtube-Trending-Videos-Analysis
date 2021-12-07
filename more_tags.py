import json
import pandas as pd
import matplotlib.pyplot as plt

countries = ["BR", "CA", "DE", "FR", "GB", "IN", "JP", "KR", "MX", "RU", "US"]

# Mostramos los tags con mas visitas en cada pais

def get_tags(country):
    r_csv = 'data/' + country + '_youtube_trending_data.csv'

    df = pd.read_csv(r_csv)

    df = df[['tags', 'view_count']]
    mask = (df.view_count <= 0)
    df = df.loc[~mask]

    df['tags'] = df['tags'].str.split('|')

    dic = {}
    for index, row in df.iterrows():
        for tag in row['tags']:
            if tag not in dic.keys():
                dic[tag] = row['view_count']
            else:
                dic[tag] += row['view_count']

    df = pd.DataFrame([[key, dic[key]] for key in dic.keys()], columns=['tags', 'view_count'])
    df = df.sort_values(by=['view_count'], ascending=False)
    print(df[0:10])


#get_tags(countries[10])


if __name__ == "__main__":
    # Arg Parser
    import argparse
    parser = argparse.ArgumentParser()
    helpRegionCode = 'Region code for the youtube videos, by default ALL. \nPossible regions:\nCA: Canada,\n\tDE: Alemania,\n\tFR: Francia,\n\tGB: Reino Unido,\n\tIN: India,\n\tJP: Japon,\n\tKR: Korea,\n\tMX: Mexico,\n\tRU: Rusia,\n\tUS: Estados Unidos'
    parser.add_argument("regionCode", help=helpRegionCode, default="ALL")
    parser.add_argument("-m", "--mode", help='console or graph, by default is console', default="console")
    args = parser.parse_args()
    # END OF ARGUMENT PARSER
    country = args.regionCode.upper()

    get_tags(country)

