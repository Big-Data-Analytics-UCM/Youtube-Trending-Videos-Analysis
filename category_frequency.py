import json
import pandas as pd
import matplotlib.pyplot as plt

countries = ["BR", "CA", "DE", "FR", "GB", "IN", "JP", "KR", "MX", "RU", "US"]

def get_categories(country):
    ruta_csv = 'data/' + country + '_youtube_trending_data.csv'
    ruta_json = 'data/' + country + '_category_id.json'

    df = pd.read_csv(ruta_csv)

    df = df[['categoryId', 'view_count']]
    mask = (df.view_count <= 0)
    df = df.loc[~mask]

    with open(ruta_json) as json_file:
        data = json.load(json_file)
        category_dict = dict()
        for item in data['items']:
            index = int(item['id'])
            category_dict[index] = item['snippet']['title']

    df = df.replace({"categoryId": category_dict})
    return df

def generar_grafica(df, region):
    if region == "GLOBAL":
        for country in countries:
            df.country.categoryId.value_counts(normalize=True).plot.bar(figsize=(15, 8), rot=25, color='orange', ec='k')
    df.categoryId.value_counts(normalize=True).plot.bar(figsize=(15, 8), rot=25, color='orange', ec='k')
    plt.xlabel("Video Category")
    plt.ylabel("Relative frequency of videos")
    plt.title("Video categories by relative frequency")
    plt.savefig("category_frequency_" + region + ".png", dpi=100)


def grafica_pais(country):
    category_df = get_categories(country)
    generar_grafica(category_df, country)

def grafica_mundial():
    categories_per_country_df = pd.DataFrame
    for country in countries:
        # categories_per_country_df.append(get_categories(country), ignore_index=True)
        categories_per_country_df.loc()
    print(categories_per_country_df)
    # generar_grafica(categories_per_country_df, "GLOBAL")


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

    if region == "ALL":
        grafica_mundial()
    else:
        grafica_pais(region)
