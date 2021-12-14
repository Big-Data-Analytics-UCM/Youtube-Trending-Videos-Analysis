import os
import sys
import argparse
import time

PROJECT_PATH = os.getcwd()

paises = ["GLOBAL", "BR", "CA", "DE", "FR", "GB", "IN", "JP", "KR", "MX", "RU", "US"]
modos = ["CONSOLA", "GRAFICA"]

def argument_parser():
	parser = argparse.ArgumentParser(description='Conoce el algoritmo de YouTube y aumenta las probabilidades de'
									 'conseguir que tu video se vuelva viral.', prog='YouTube_Trending_Videos')
	return parser.parse_args()


def menu_options():
	options = dict()
	options.update({'1': "Gráfica de categorías en tendencia."})
	options.update({'2': "Gráfica para analizar la hora de publicación de un video por frecuencia."})
	options.update({'3': "Gráfica para analizar la longitud del título del video."})
	options.update({'4': "Gráfica para analizar el porcentaje de mayúsculas en los títulos de los videos."})
	options.update({'5': "Gráfica de correlación entre número de visitas y likes."})
	options.update({'6': "Gráfica de correlación entre número de visitas y dislikes."})
	options.update({'7': "Top 10 videos más vistos."})
	options.update({'8': "Top 10 videos con más comentarios."})
	options.update({'9': "Top 10 videos con más Me Gusta."})
	options.update({'10': "Top 10 tags con más visualizaciones por país."})
	options.update({'0': "Exit"})
	return options


def menu_actions():
	actions = dict()
	actions.update({'1': "scripts/category_frequency.py"})
	actions.update({'2': "scripts/published_at_frequency.py"})
	actions.update({'3': "scripts/title_length_analysis.py"})
	actions.update({'4': "scripts/title_caps_analysis.py"})
	actions.update({'5': "scripts/correlation_likes.py"})
	actions.update({'6': "scripts/correlation_dislikes.py"})
	actions.update({'7': "scripts/top10_most_views.py"})
	actions.update({'8': "scripts/most_commented.py"})
	actions.update({'9': "scripts/most_liked.py"})
	actions.update({'10': "scripts/more_tags.py"})
	actions.update({'0': ""})
	return actions


def exit_program():
	exit_msg = "Saliendo..."

	print(exit_msg)
	sys.exit(0)
	pass


def execute_menu_option(option):
	if option == '0':
		exit_program()
	actions = menu_actions()
	pais = str(input("Indique el código del país ('GLOBAL' para análisis mundial): ")).upper()
	while pais not in paises:
		print('\nLas posibles regiones son:\n\tBR: Brasil\n\tCA: Canadá,\n\tDE: Alemania,\n\tFR: Francia,'
			  '\n\tGB: Reino Unido,\n\tIN: India,\n\tJP: Japón,\n\tKR: Korea,\n\tMX: México,\n\tRU: Rusia,'
			  '\n\tUS: Estados Unidos')
		pais = str(input("Indique el código del país ('GLOBAL' para análisis mundial): ")).upper()    
	
	if option == '1':
		modo = str(input("Indique el modo en el que quiere ver el resultado, CONSOLA o GRAFICA: ")).upper()
		while modo not in modos:
			modo = str(input("Indique el modo en el que quiere ver el resultado, CONSOLA o GRAFICA: ")).upper() 
	else:
		modo = "GRAFICA"
	path = actions[option]
	cmd = "spark-submit \"{PATH}\" -m {MODO} {COUNTRY}".format(PATH=path, MODO=modo, COUNTRY=pais)
	inicio = time.time()
	os.system(cmd)
	fin = time.time()
	print("\nSegundos que tarda en ejercutarse la función: " + str(fin - inicio) + "\n")


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
	print(welcome)
	options_dict = menu_options()
	while menu(options_dict):
		pass

	   
