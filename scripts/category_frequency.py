import json
import sys
from pyspark import SparkConf, SparkContext, SQLContext
import pandas as pd
import matplotlib.pyplot as plt

countries = ["BR", "CA", "DE", "FR", "GB", "IN", "JP", "KR", "MX", "RU", "US"]

def category_frequency(region, mode):
    conf = SparkConf().setMaster('local').setAppName('Top_Category')
    sc = SparkContext(conf=conf)
    sql_context = SQLContext(sc)

    if mode == "CONSOLA" and region == "GLOBAL":
        consola_global(sql_context)
    elif mode == "CONSOLA" and region != "GLOBAL":
        consola_pais(region, sql_context)
    elif mode == "GRAFICA" and region == "GLOBAL":
        grafica_global()
    else:
        grafica_pais(region)


def get_categories(country):
    ruta_csv = 'data/' + country + '_youtube_trending_data.csv'
    ruta_json = 'data/' + country + '_category_id.json'

    df = pd.read_csv(ruta_csv, engine='python', error_bad_lines=False)

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


def consola_pais(country, sql_context):
    pass


def consola_global(sql_context):
    pass


def grafica_pais(country):
    category_df = get_categories(country)
    generar_grafica(category_df, country)


def grafica_global():
    categories_per_country_df = pd.DataFrame()
    for country in countries:
        categories_per_country_df = categories_per_country_df.append(get_categories(country), ignore_index=True)

    generar_grafica(categories_per_country_df, "GLOBAL")


def generar_grafica(df, region):
    print("Generando gráfica...")
    df.categoryId.value_counts(normalize=True).plot.bar(figsize=(15, 10), rot=25, color='orange', ec='k')
    plt.xlabel("Video Category")
    plt.ylabel("Relative frequency of videos")
    plt.title("Video categories by relative frequency in")
    plt.title("Video categories by relative frequency ")
    plt.savefig("outData/category_frequency_" + region + ".png", dpi=100)
    print("Gráfica guardada en outData/category_frecuency" + region + ".png")

if __name__ == "__main__":
    # ARGUMENT PARSER
    import argparse

    parser = argparse.ArgumentParser()
    help_region_code = 'Código de región para los videos de YouTube; por defecto, GLOBAL.' \
                       '\nPosibles regiones:\nBR: Brasil\n\tCA: Canadá,\n\tDE: Alemania,\n\tFR: Francia,' \
                       '\n\tGB: Reino Unido,\n\tIN: India,\n\tJP: Japón,\n\tKR: Korea,\n\tMX: México,\n\tRU: Rusia,' \
                       '\n\tUS: Estados Unidos'
    help_mode = 'Selecciona el modo de visualización: GRAFICO o CONSOLA; por defecto, CONSOLA'
    parser.add_argument("regionCode", help=help_region_code, default="GLOBAL")
    parser.add_argument("-m", "--mode", help=help_mode, default="GRAFICO")
    args = parser.parse_args()
    # END OF ARGUMENT PARSER

    region = args.regionCode.upper()
    mode = args.mode.upper()

    if region not in countries + ["GLOBAL", ""]:
        print(help_region_code)
        sys.exit(0)

    if mode not in ["CONSOLA", "GRAFICO", ""]:
        print(help_mode)
        sys.exit(0)

    category_frequency(region, mode)

