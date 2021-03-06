import pandas as pd
import matplotlib.pyplot as plt

countries = ["BR", "CA", "DE", "FR", "GB", "IN", "JP", "KR", "MX", "RU", "US"]

def get_info(country): 
    ruta_csv = 'data/' + country + '_youtube_trending_data.csv'
    df = pd.read_csv(ruta_csv, engine='python', error_bad_lines=False)

    mask = (df.view_count <= 0)
    df = df.loc[~mask]

    df.drop(['channelId', 'tags', 'thumbnail_link', 'comments_disabled', 'ratings_disabled', 'description'], axis=1,
            inplace=True)

    df['len_title'] = df.title.apply(len)
    return df


def generar_grafica(df, country):
    print("Generando gráfica...")

    plt.figure(figsize=[11, 9])
    plt.hist(df['len_title'], color='orange', rwidth=0.9)

    median_length = df['len_title'].mean()
    plt.axvline(median_length, color='#fc4f30', label='Media')

    plt.legend()
    plt.grid(axis='y')
    plt.title('Número de apariciones según número de caracteres en el título',  fontsize=15)
    plt.xlabel('Número de caracteres en el título')
    plt.ylabel('Número de apariciones')
    plt.savefig("outData/title_length_frequency_" + country + ".png", dpi=100)
    print("Gráfica guardada en outData/title_length_frequency_" + country + ".png")


def grafica_pais(country):
    category_df = get_info(country)
    generar_grafica(category_df, country)


def grafica_mundial():
    title_df = pd.DataFrame()
    for country in countries:
        title_df = title_df.append(get_info(country), ignore_index=True)

    generar_grafica(title_df, "GLOBAL")


if __name__ == "__main__":
    # ARGUMENT PARSER
    import argparse

    parser = argparse.ArgumentParser()
    helpRegionCode = 'Código de región para los videos de YouTube; por defecto, GLOBAL.' \
                     '\nPosibles regiones:\nBR: Brasil\n\tCA: Canadá,\n\tDE: Alemania,\n\tFR: Francia,' \
                     '\n\tGB: Reino Unido,\n\tIN: India,\n\tJP: Japón,\n\tKR: Korea,\n\tMX: México,\n\tRU: Rusia,' \
                     '\n\tUS: Estados Unidos'
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
