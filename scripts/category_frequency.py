import json
import sys
from pyspark import SparkConf, SparkContext, SQLContext
from pyspark.sql.functions import col, create_map, lit
from itertools import chain
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
        consola_pais(region, sql_context, False)
    elif mode == "GRAFICA" and region == "GLOBAL":
        grafica_global()
    else:
        grafica_pais(region, False)


def get_categories(country):
    # ruta_csv = 'data/' + country + '_youtube_trending_data.csv'
    ruta_json = 'data/' + country + '_category_id.json'

    # df = pd.read_csv(ruta_csv, engine='python', error_bad_lines=False)
    #
    # df = df[['categoryId', 'view_count']]
    # mask = (df.view_count <= 0)
    # df = df.loc[~mask]

    with open(ruta_json) as json_file:
        data = json.load(json_file)
        category_dict = dict()
        for item in data['items']:
            index = int(item['id'])
            category_dict[index] = item['snippet']['title']

    # df = df.replace({"categoryId": category_dict})
    return category_dict


def consola_pais(country, sql_context, is_global):
    ruta_csv = 'data/' + country + '_youtube_trending_data.csv'
    df = sql_context.read.csv(ruta_csv, header=True, sep=',', encoding='utf-8')
    categorias = df.groupBy("categoryId").count()
    category_dict = get_categories(country)

    mapping_expr = create_map([lit(x) for x in chain(*category_dict.items())])
    categorias = categorias.withColumn('categoryId', mapping_expr[categorias['categoryId']])
    categorias = categorias.filter(categorias.categoryId.isNotNull())
    if is_global is not True:
        categorias.sort("count",ascending = False).show()
    else:
        return categorias.sort("count",ascending = False)


def consola_global(sql_context):
    dataframe = pd.DataFrame()
    for country in countries:
        dataframe = dataframe.append(consola_pais(country, sql_context, True), ignore_index = True)
    
    print(dataframe)
    

    


def grafica_pais(country, is_global):
    ruta_csv = 'data/' + country + '_youtube_trending_data.csv'

    df = pd.read_csv(ruta_csv, engine='python', error_bad_lines=False)

    df = df[['categoryId', 'view_count']]
    mask = (df.view_count <= 0)
    df = df.loc[~mask]

    category_df = df.replace({"categoryId": get_categories(country)})
    if is_global is not True:
        generar_grafica(category_df, country)
    else:
    	return category_df


def grafica_global():
    categories_per_country_df = pd.DataFrame()
    for country in countries:        
        categories_per_country_df = categories_per_country_df.append(grafica_pais(country, True), ignore_index = True)

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
    parser.add_argument("-m", "--mode", help=help_mode, default="GRAFICA")
    args = parser.parse_args()
    # END OF ARGUMENT PARSER

    region = args.regionCode.upper()
    mode = args.mode.upper()

    if region not in countries + ["GLOBAL", ""]:
        print(help_region_code)
        sys.exit(0)

    if mode not in ["CONSOLA", "GRAFICA", ""]:
        print(help_mode)
        sys.exit(0)

    category_frequency(region, mode)
