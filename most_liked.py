import pandas as pd

countries = ["BR", "CA", "DE", "FR", "GB", "IN", "JP", "KR", "MX", "RU", "US"]

def get_likes(country):
    ruta_csv = 'data/' + country + '_youtube_trending_data.csv'

    df = pd.read_csv(ruta_csv)
    df = df[['title', 'likes']]
    mask = (df.likes <= 0)
    df = df.loc[~mask]

    df = df.sort_values(by=['likes'], ascending=False).drop_duplicates(subset=['title'])
    return df.head(10)


def get_local(region):
    print(get_likes(region).to_string(index=False))


def get_global():
    global_df = pd.DataFrame()
    for reg in countries:
        region_df = get_likes(reg)
        region_df = region_df.assign(region=[reg, reg, reg, reg, reg, reg, reg, reg, reg, reg])
        global_df = global_df.append(region_df, ignore_index=True)
    global_df = global_df.sort_values(by=['likes'], ascending = False).drop_duplicates(subset=['title']).head(10)
    print(global_df.to_string(index = False))


if __name__ == "__main__":
    # Arg Parser
    import argparse
    parser = argparse.ArgumentParser()
    helpRegionCode = 'Region code for the youtube videos, by default GLOBAL.\nPossible regions:\nCA: Canada,\n\tDE: Alemania,\n\tFR: Francia,\n\tGB: Reino Unido,\n\tIN: India,\n\tJP: Japon,\n\tKR: Korea,\n\tMX: Mexico,\n\tRU: Rusia,\n\tUS: Estados Unidos'
    parser.add_argument("regionCode", help=helpRegionCode, default="GLOBAL")
    parser.add_argument("-m", "--mode", help='console or graph, by default is console', default="console")
    args = parser.parse_args()
    # END OF ARGUMENT PARSER
    region = args.regionCode.upper()

    if region == "GLOBAL":
        get_global()
    else:
        get_local(region)
