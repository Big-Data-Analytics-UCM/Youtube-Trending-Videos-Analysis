import json
import pandas as pd
import matplotlib.pyplot as plt

def grafica_pais(country):
    ruta_json = country + '_category_id.json'
    ruta_csv = country + '_youtube_trending_data.csv'
    with open(ruta_json) as json_file:
        data = json.load(json_file)
        store_list = dict()
        for item in data['items']:
            index = int(item['id'])
            store_list[index] = item['snippet']['title']

    df = pd.read_csv(ruta_csv, parse_dates=['publishedAt', 'trending_date'])

    df = df.replace({"categoryId": store_list})

    mask = (df.view_count <= 0)
    df = df.loc[~mask]

    df.categoryId.value_counts(normalize=True).plot.bar(figsize=(15, 8), rot=25, color='orange', ec='k')
    plt.xlabel("Video Category")
    plt.ylabel("Relative frequency of videos")
    plt.title("Video categories by relative frequency")
    plt.savefig("category_frequency_" + country + ".png", dpi=100)


if __name__ == "__main__":
    # ARGUMENT PARSER
    import argparse

    parser = argparse.ArgumentParser()
    helpRegionCode = 'Region code for the youtube videos, by default ALL.\nPossible regions:\nCA: Canada,\n\tDE: Alemania,\n\tFR: Francia,\n\tGB: Reino Unido,\n\tIN: India,\n\tJP: Japon,\n\tKR: Korea,\n\tMX: Mexico,\n\tRU: Rusia,\n\tUS: Estados Unidos'
    parser.add_argument("regionCode", help=helpRegionCode, default="ALL")
    parser.add_argument("-m", "--mode", help='console or graph, by default is console', default="console")
    args = parser.parse_args()
    # END OF ARGUMENT PARSER
    region = args.regionCode.upper()
    mode = args.mode.upper()

    grafica_pais(region)
