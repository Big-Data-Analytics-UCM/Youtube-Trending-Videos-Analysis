import os
import sys
import argparse

# PROJECT_PATH = os.path.dirname(os.getcwd())
PROJECT_PATH = os.getcwd()

API_KEY = "AIzaSyCXwEu_N5gbvyD97-uVQCH7FyQq0LmtNMo"

def argument_parser():
    parser = argparse.ArgumentParser(description='Conoce el algoritmo de YouTube y aumenta las probabilidades de'
                                     'conseguir que tu video se vuelva viral.', prog='YouTube_Trending_Videos')
    # parser.add_argument('--region', help='Regions: IN (India), US (EEUU), GB (Gran Bretaña),DE (Alemania), '
    #                                     'CA (Canadá), FR (Francia), RU (Rusia), BR (Brasil), MX (Mexico), KR (Korea) '
    #                                     'y JP (Japón)', default="ALL")
    return parser.parse_args()


def menu_options():
    options = dict()
    options.update({'1': "Gráfica de categorías en tendencia"})
    options.update({'2': "Gráfica para analizar la longitud del título del video"})
    options.update({'3': "Gráfica para analizar la hora de publicación de un video por frecuencia"})
    options.update({'4': "Gráfica para analizar la hora de publicación de un video por likes"})
    # options['1'] = "Media de visitas por mes."
    # options['2'] = "Media de visitas por año."
    # options['3'] = "Categoria con mas videos."
    # options['4'] = "Top 10 de videos mas vistos."
    # options['5'] = "Dia de la semana con mas visitas."
    # options['6'] = "Videos con mayor cantidad de likes."
    # options['7'] = "Videos con mayor cantidad de comentarios."
    # options['8'] = "Gráfica de categorías en tendencia por país."
    # options['9'] = "Gráfica de categorias mundial."
    # options['10'] = "Cuadro de categorias por país."
    # options['11'] = "Cuadro de categorias mundial."
    # options['0'] = "Exit"
    options.update({'0': "Exit"})
    return options


def menu_actions():
    actions = dict()
    actions.update({'1': grafico_categoria})
    actions.update({'2': grafico_long_titulo})
    actions.update({'3': grafico_hora_publicacion_frecuencia})
    actions.update({'4': grafico_hora_publicacion_visitas})
    # actions['1'] = averageVisitsPerMonth
    # actions['2'] = averageVisitsPerYear
    # actions['3'] = categoryWithMoreVideos
    # actions['4'] = top10VideosWithMore
    # actions['5'] = weekdayWithMoreVisits
    # actions['6'] = videosWithMoreLikes
    # actions['7'] = videosWithMoreComments
    # actions['8'] = grafico_categoria_pais
    # actions['9'] = categoryGraphWorldwide
    # actions['10'] = showCategoriesByCountry
    # actions['11'] = showCategoriesWorldwide
    actions['0'] = exit_program
    return actions

def grafico_categoria():
    pais = str(input("Indique el código del país ('GLOBAL' para análisis mundial): "))
    path = "category_frequency.py"
    cmd = "python3 \"{PATH}\" -m graph {COUNTRY}".format(PATH=path, COUNTRY=pais)
    os.system(cmd)

def grafico_long_titulo():
    pais = str(input("Indique el código del país ('GLOBAL' para análisis mundial): "))
    path = "title_length_analysis.py"
    cmd = "python3 \"{PATH}\" -m graph {COUNTRY}".format(PATH=path, COUNTRY=pais)
    os.system(cmd)

# def grafico_categoria_pais():
#     pais = str(input("Indique el código del país: "))
#     # os.system("python3 liveData.py {COUNTRY}".format(COUNTRY=pais))
#     # path = os.path.join(PROJECT_PATH, "category_frequency.py")
#     path = "category_frequency.py"
#     # cmd = "spark-submit \"{PATH}\" -m graph {COUNTRY}".format(PATH=path, COUNTRY=pais)
#     cmd = "python3 \"{PATH}\" -m graph {COUNTRY}".format(PATH=path, COUNTRY=pais)
#     os.system(cmd)

#
# def grafico_categoria_mundial():
#     # path = os.path.join(PROJECT_PATH, "scripts", "topCategories.py")
#     path = os.path.join(PROJECT_PATH, "category_frequency.py")
#     # cmd = "spark-submit \"{PATH}\" -m graph ALL".format(PATH=path)
#     cmd = "python3 \"{PATH}\" -m graph ALL".format(PATH=path)
#     os.system(cmd)




def grafico_hora_publicacion_frecuencia():
    pass


def grafico_hora_publicacion_visitas():
    pass
    #pais = str(input("Indique el código del país: "))
    # os.system("python3 liveData.py {COUNTRY}".format(COUNTRY=pais))
    # path = os.path.join(PROJECT_PATH, "category_frequency.py")
    #path = "category_frequency.py"
    # cmd = "spark-submit \"{PATH}\" -m graph {COUNTRY}".format(PATH=path, COUNTRY=pais)
    #cmd = "python3 \"{PATH}\" -m graph {COUNTRY}".format(PATH=path, COUNTRY=pais)
    #os.system(cmd)





def exit_program():
    exit_msg = "Saliendo..."

    print(exit_msg)
    sys.exit(0)
    pass


def execute_menu_option(option):
    actions = menu_actions()
    function = actions[option]
    function()
    pass


def menu(options):
    # Print options
    for code, value in options.items():
        print(code, value)

    # Ask for an option
    option = str(input("select option: "))

    # Verify if its a valid option and execute it
    if option in options.keys():
        execute_menu_option(option)
    else:
        # print(bcolors.FAIL + "Invalid option" + bcolors.ENDC)
        print("Invalid option.")

    return True


if __name__ == "__main__":
    welcome = """
         ___      ___                ._____________.
         \  \    /  /                |_____.  .____|
          \  \  /  /                       |  |
           \  \/  /.________.  .__.  .__.  |  |  .__.  .__.  .________.  .________.
            \    / |   __   |  |  |  |  |  |  |  |  |  |  |  |        |  |  ._____|                
             |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   O   /   |  |__.
             |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |       \   |  .__|
             |  |  |  |__|  |  |  |__|  |  |  |  |  |__|  |  |   O    |  |  |_____.
             |__|  |________|  |________|  |__|  |________|  |________|  |________|
    """
    args = argument_parser()
    # os.system("python3 liveData.py {COUNTRY}".format(COUNTRY=args.regionCode.upper()))
    print(welcome)
    options_dict = menu_options()
    while menu(options_dict):
        pass
