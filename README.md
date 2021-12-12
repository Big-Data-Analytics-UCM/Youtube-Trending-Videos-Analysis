# Proyecto_Cloud
Proyecto Final de la asignatura Optativa Cloud y Big Data - Facultad de Informática UCM 2021/22 

###Cómo configurarlo
abrir una vm en el cloud console y conectarse por ssh
- sudo apt update
- sudo apt install python3 python3-dev python3-venv
- instalar java, spark, git, pip3 (no se si algo mas)
- git clone <url repo>
- cd <your-project>
- crear y activar un entorno virtual
    - python3 -m venv env
    - source env/bin/activate
- pip3 install --upgrade pip
- pip3 install wheel
- pip3 install google-cloud-storage
- install required packages:
    - pip3 install -r requirements.txt

listo