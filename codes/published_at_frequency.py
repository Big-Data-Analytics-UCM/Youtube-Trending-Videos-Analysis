#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

countries = ["BR", "CA", "DE", "FR", "GB", "IN", "JP", "KR", "MX", "RU", "US"]

def published_at_frequency(country):
    ruta = 'data/' + country + '_youtube_trending_data.csv'
    df = pd.read_csv(ruta, parse_dates=['publishedAt', 'trending_date'], engine='python', on_bad_lines='skip')

    mask = (df.view_count <= 0)
    df = df.loc[~mask]

    df.rename(columns={'trending_date': 'trendingAt'}, inplace=True)

    df.insert(loc=3, column='published_hour', value=df.publishedAt.dt.hour)
    return df


def generar_grafica(df, country):
    df.published_hour.value_counts(normalize=True).sort_index().plot.bar(figsize=[15, 8], rot=0, color='orange', ec='k')
    plt.xlabel("Published Hour")
    plt.ylabel("Relative frequency of videos")
    plt.title("Published Hour by relative frequency")
    plt.savefig("outData/published_at_frequency_" + country + ".png", dpi=100)


def grafica_pais(country):
    category_df = published_at_frequency(country)
    generar_grafica(category_df, country)


def grafica_mundial():
    hour_df = pd.DataFrame()
    for country in countries:
        hour_df = hour_df.append(published_at_frequency(country), ignore_index=True)

    generar_grafica(hour_df, "GLOBAL")


if __name__ == "__main__":
    # ARGUMENT PARSER
    import argparse

    parser = argparse.ArgumentParser()
    helpRegionCode = 'Region code for the youtube videos, by default ALL.\nPossible regions:\nBR: Brasil,\n\tCA: Canada,\n\tDE: Alemania,\n\tFR: Francia,\n\tGB: Reino Unido,\n\tIN: India,\n\tJP: Japon,\n\tKR: Korea,\n\tMX: Mexico,\n\tRU: Rusia,\n\tUS: Estados Unidos'
    parser.add_argument("regionCode", help=helpRegionCode, default="GLOBAL")
    parser.add_argument("-m", "--mode", help='console or graph, by default is graph', default="graph")
    args = parser.parse_args()
    # END OF ARGUMENT PARSER

    region = args.regionCode.upper()
    mode = args.mode.upper()

    if region == "GLOBAL":
        grafica_mundial()
    else:
        grafica_pais(region)
