import pandas as pd


countries = ["BR", "CA", "DE", "FR", "GB", "IN", "JP", "KR", "MX", "RU", "US"]

# Mostramos los tags con mas visitas en cada pais

def get_tags(country):
    r_csv = 'data/' + country + '_youtube_trending_data.csv'

    df = pd.read_csv(r_csv, engine='python', error_bad_lines=False)

    df = df[['tags', 'view_count']]
    mask = (df.view_count <= 0)
    df = df.loc[~mask]

    df['tags'] = df['tags'].str.split('|')

    dic = {}
    for index, row in df.iterrows():
        for tag in row['tags']:
            if tag not in dic.keys():
                dic[tag] = row['view_count']
            else:
                dic[tag] += row['view_count']

    df = pd.DataFrame([[key, dic[key]] for key in dic.keys()], columns=['tags', 'view_count'])
    df = df.sort_values(by=['view_count'], ascending=False).head(10)
    return df.head(10).reset_index(drop=True)

def get_table(regionDF, region):
    #Creates the HTML Struct for the output file
    table = "<html>\n"
    table+= "<head>\n"
    #Bootstrap Linking
    table+= "<link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3\" crossorigin=\"anonymous\">\n"
    table+= "</head>\n"
    table+= "<body>\n"
    table+="<section class=\"container-md\">\n"
    #Converting output DataFrame to a HTML table, and stilizing with bootstrap
    dfOut = regionDF.to_html()
    dfOut = dfOut.replace("<table border=\"1\" class=\"dataframe\">", "<table class=\"table table-dark table-striped\">")
    dfOut = dfOut.replace("<tr style=\"text-align: right;\">", "<tr>")
    dfOut = dfOut.replace("<th>title</th>", "<th>Nombre del tag</th>")
    dfOut = dfOut.replace("<th>likes</th>", "<th>Número de visualizaciones</th>")
    dfOut = dfOut.replace("<th>region</th>", "<th>Región</th>")
    table+= dfOut
    table+="</section>\n"
    table+= "</body>\n"
    table+= "</html>\n"
    #Writes the final HTML code
    outFile = open("outData/more_tags_" + region + ".html", "w")
    outFile.write(table)
    outFile.close()

def get_global():
    global_df = pd.DataFrame()
    for reg in countries:
        region_df = get_tags(reg)
        region_df = region_df.assign(region=[reg, reg, reg, reg, reg, reg, reg, reg, reg, reg])
        global_df = global_df.append(region_df, ignore_index=True)
    global_df = global_df.sort_values(by=['view_count'], ascending=False).head(10)
    global_df = global_df.reset_index(drop=True)
    get_table(global_df, "GLOBAL")


if __name__ == "__main__":
    # Arg Parser
    import argparse
    parser = argparse.ArgumentParser()
    helpRegionCode = 'Region code for the youtube videos, by default ALL. \nPossible regions:\nCA: Canada,\n\tDE: Alemania,\n\tFR: Francia,\n\tGB: Reino Unido,\n\tIN: India,\n\tJP: Japon,\n\tKR: Korea,\n\tMX: Mexico,\n\tRU: Rusia,\n\tUS: Estados Unidos'
    parser.add_argument("regionCode", help=helpRegionCode, default="ALL")
    parser.add_argument("-m", "--mode", help='console or graph, by default is console', default="console")
    args = parser.parse_args()
    # END OF ARGUMENT PARSER
    region = args.regionCode.upper()

    if region == "GLOBAL":
        get_global()
    else:
        get_table(get_tags(region), region)



