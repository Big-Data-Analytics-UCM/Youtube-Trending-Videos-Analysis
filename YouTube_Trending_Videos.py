import os
import sys
import argparse

PROJECT_PATH = os.getcwd()

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
    options.update({'4': "Gráfica para analizar la hora de publicación de un video por visitas (no implem.)"})
    options.update({'5': "Top 10 videos mas vistos"})
    options.update({'6': "Videos con mas comentarios"})
    options.update({'7': "Videos con mas Me Gusta"})
    options.update({'8': "Gráfica de correlación entre número de visitas y likes"})
    options.update({'9': "Gráfica de correlación entre número de visitas y dislikes"})
    options.update({'10': "Tags con mas visuzalizaciones por pais."})
    options.update({'0': "Exit"})
    return options


def menu_actions():
    actions = dict()
    actions.update({'1': "codes/category_frequency.py"})
    actions.update({'2': "codes/title_length_analysis.py"})
    actions.update({'3': "codes/published_at_frequency.py"})
    # actions.update({'4': grafico_hora_publicacion_visitas})
    actions.update({'5': "codes/top10_most_views.py"})
    actions.update({'6': "codes/most_commented.py"})
    actions.update({'7': "codes/most_liked.py"})
    actions.update({'8': "codes/correlation_likes.py"})
    actions.update({'9': "codes/correlation_dislikes.py"})
    actions.update({'10': "codes/more_tags.py"})
    actions.update({'0': exit_program})
    return actions


def grafico_hora_publicacion_visitas():
    pass


def exit_program():
    exit_msg = "Saliendo..."

    print(exit_msg)
    sys.exit(0)
    pass

def execute_menu_option(option):
    if option == '0':
        exit_program()
    actions = menu_actions()
    pais = str(input("Indique el código del país ('GLOBAL' para análisis mundial): "))
    path = actions[option]
    cmd = "python3 \"{PATH}\" -m graph {COUNTRY}".format(PATH=path, COUNTRY=pais)
    os.system(cmd)


def menu(options):
    # Imprime el menú, solicita al usuario una opción
    # y verifica si esta es correcta

    for code, value in options.items():
        print(code, value)

    option = str(input("Seleccione una opción del menú: "))

    if option in options.keys():
        execute_menu_option(option)
    else:
        print("Opción inválida. Inténtelo de nuevo")
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
