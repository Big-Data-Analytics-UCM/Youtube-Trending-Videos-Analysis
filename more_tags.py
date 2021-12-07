import json
import pandas as pan
import matplotlib.pyplot as plt

countries = ["BR", "CA", "DE", "FR", "GB", "IN", "JP", "KR", "MX", "RU", "US"]

def get_likes(country):
    r_csv = 'data/' + country + '_youtube_trending_data.csv'
    r_json = 'data/' + country + '_category_id.json'

    df = pan.read_csv(r_csv)

    df = df[['tags', 'view_count']]
    mask = (df.view_count <= 0)
    df = df.loc[~mask]

    """""
    with open(r_json) as json_file:
        data = json.load(json_file)
        tag_dict = dict()
        for item in data['items']:
            index = int(item['id'])
            tag_dict[index] = item['etag']
    df = df.replace({"tagId": tag_dict})
    """

    df = df.sort_values(by=['view_count'], ascending=False).drop_duplicates(subset=['tags'])
    print(df)


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

    get_likes(country)
