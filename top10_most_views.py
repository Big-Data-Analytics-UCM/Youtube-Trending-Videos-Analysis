import json
import pandas as pd
import matplotlib.pyplot as plt

countries = ["BR", "CA", "DE", "FR", "GB", "IN", "JP", "KR", "MX", "RU", "US"]

def get_view_count(country):
    ruta_csv = 'data/' + country + '_youtube_trending_data.csv'
    ruta_json = 'data/' + country + '_category_id.json'

    df = pd.read_csv(ruta_csv)
    df = df[['title', 'view_count']]
    mask = (df.view_count <= 0)
    df = df.loc[~mask]

    df = df.sort_values(by=['view_count'], ascending=False).drop_duplicates(subset=['title'])
    res = df.head(10)
    return res

def get_local(region):
    print(get_view_count(region).to_string(index = False))

def get_global():
    globalDf = pd.DataFrame()
    for reg in countries:
        regionDf = get_view_count(reg)
        regionDf = regionDf.assign(region = [reg, reg, reg, reg, reg, reg, reg, reg, reg, reg])
        globalDf = globalDf.append(regionDf, ignore_index=True)
    globalDf = globalDf.sort_values(by=['view_count'], ascending = False).drop_duplicates(subset=['title']).head(10)
    print(globalDf.to_string(index = False))

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