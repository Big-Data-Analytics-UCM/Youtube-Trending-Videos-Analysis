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
    options.update({'5': "Top 10 videos mas vistos"})
    options.update({'6': "Videos con mas comentarios"})
    options.update({'7': "Videos con mas Me Gusta"})
    options.update({'8': "Gráfica de correlación entre número de visitas y likes"})
    options.update({'9': "Gráfica de correlación entre número de visitas y dislikes"})
    options.update({'0': "Exit"})
    return options


def menu_actions():
    actions = dict()
    actions.update({'1': grafico_categoria})
    actions.update({'2': grafico_long_titulo})
    actions.update({'3': grafico_hora_publicacion_frecuencia})
    actions.update({'4': grafico_hora_publicacion_visitas})
    actions.update({'5': videos_mas_vistos})
    actions.update({'6': videos_mas_comentados})
    actions.update({'7': videos_mas_gustados})
    actions.update({'8': grafico_correlacion_likes})
    actions.update({'9': grafico_correlacion_dislikes})
    actions['0'] = exit_program
    return actions

def videos_mas_vistos():
    pais = str(input("Indique el código del país ('GLOBAL' para análisis mundial): "))
    path = "top10_most_views.py"
    cmd = "python3 \"{PATH}\" -m graph {COUNTRY}".format(PATH=path, COUNTRY=pais)
    os.system(cmd)

def videos_mas_comentados():
    pais = str(input("Indique el código del país ('GLOBAL' para análisis mundial): "))
    path = "most_commented.py"
    cmd = "python3 \"{PATH}\" -m graph {COUNTRY}".format(PATH=path, COUNTRY=pais)
    os.system(cmd)

def videos_mas_gustados():
    pais = str(input("Indique el código del país ('GLOBAL' para análisis mundial): "))
    path = "most_liked.py"
    cmd = "python3 \"{PATH}\" -m graph {COUNTRY}".format(PATH=path, COUNTRY=pais)
    os.system(cmd)

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

def grafico_hora_publicacion_frecuencia():
    pais = str(input("Indique el código del país ('GLOBAL' para análisis mundial): "))
    path = "published_at_frequency.py"
    cmd = "python3 \"{PATH}\" -m graph {COUNTRY}".format(PATH=path, COUNTRY=pais)
    os.system(cmd)

def grafico_hora_publicacion_visitas():
    pass
    #pais = str(input("Indique el código del país: "))
    # os.system("python3 liveData.py {COUNTRY}".format(COUNTRY=pais))
    # path = os.path.join(PROJECT_PATH, "category_frequency.py")
    #path = "category_frequency.py"
    # cmd = "spark-submit \"{PATH}\" -m graph {COUNTRY}".format(PATH=path, COUNTRY=pais)
    #cmd = "python3 \"{PATH}\" -m graph {COUNTRY}".format(PATH=path, COUNTRY=pais)
    #os.system(cmd)

def grafico_correlacion_likes():
    pais = str(input("Indique el código del país ('GLOBAL' para análisis mundial): "))
    path = "correlation_likes.py"
    cmd = "python3 \"{PATH}\" -m graph {COUNTRY}".format(PATH=path, COUNTRY=pais)
    os.system(cmd)

def grafico_correlacion_dislikes():
pais = str(input("Indique el código del país ('GLOBAL' para análisis mundial): "))
path = "correlation_dislikes.py"
cmd = "python3 \"{PATH}\" -m graph {COUNTRY}".format(PATH=path, COUNTRY=pais)
os.system(cmd)

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
