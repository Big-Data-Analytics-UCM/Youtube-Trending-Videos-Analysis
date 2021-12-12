import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

countries = ["BR", "CA", "DE", "FR", "GB", "IN", "JP", "KR", "MX", "RU", "US"]

def get_info(country): 
    ruta_csv = 'data/' + country + '_youtube_trending_data.csv'
    df = pd.read_csv(ruta_csv, engine='python', error_bad_lines=False)

    mask = (df.view_count <= 0)
    df = df.loc[~mask]

    sub_df = df.groupby('title')[['view_count', 'likes', 'dislikes','comment_count']].max()
    return sub_df

def generar_grafica(df, region):
    print("Generando gráfica...")
    corr = df.dislikes.corr(df.view_count)
    sns.lmplot(data=df, x='view_count', y='dislikes', scatter_kws={'color': 'orange', 'alpha': 0.2,
               's': df.dislikes/10000}, height=6, aspect=1.5)
    plt.title(f"Regression plot between Views and Dislikes - correlation: {corr:.3f}",
              fontdict={'size': 18, 'color': 'blue'})
    plt.savefig("outData/correlation_dislikes_" + region + ".png", dpi=100)
    print("Gráfica guardada en outData/correlation_dislikes_" + region + ".png")


def grafica_pais(country):
    correlation_df = get_info(country)
    generar_grafica(correlation_df, country)


def grafica_mundial():
    correlation_per_country_df = pd.DataFrame()
    for country in countries:
        correlation_per_country_df = correlation_per_country_df.append(get_info(country), ignore_index=True)

    generar_grafica(correlation_per_country_df, "GLOBAL")


if __name__ == "__main__":
    # ARGUMENT PARSER
    import argparse

    parser = argparse.ArgumentParser()
    helpRegionCode = 'Código de región para los videos de YouTube; por defecto, GLOBAL.' \
                     '\nPosibles regiones:\nCA: Canadá,\n\tDE: Alemania,\n\tFR: Francia,\n\tGB: Reino Unido,' \
                     '\n\tIN: India,\n\tJP: Japón,\n\tKR: Korea,\n\tMX: México,\n\tRU: Rusia,\n\tUS: Estados Unidos'
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
