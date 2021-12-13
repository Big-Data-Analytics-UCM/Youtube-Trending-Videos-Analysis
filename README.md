# Análisis predictivo de tendencias virales en vídeos de Youtube.
Proyecto Final de la asignatura Optativa Cloud y Big Data - Facultad de Informática UCM 2021/22 

### Objetivo
El objetivo de este proyecto es obtener un análisis predictivo sobre un dataset de datos sobre los videos de tendencias diarias de YouTube. Se incluyen datos para las regiones India, EE. UU., Gran Bretaña, Alemania, Canadá, Francia, Rusia, Brasil, México, Corea del Sur , y Japón, respectivamente, con hasta 200 videos de tendencias listados por día. Los datos incluyen el título del video, el título del canal, la hora de publicación, las etiquetas, las vistas, los gustos y los disgustos, la descripción y el recuento de comentarios.

### Requisitos previos para configurar el proyecto

* Abrir una máquina virtual en cloud console y conectarse por SSH.

* Introducir los siguientes comandos:

`sudo apt update`

`sudo apt install python3 python3-dev python3-venv`

* Instalar java:

`sudo apt install default-jre`

* Instalar Spark:

`curl -O https://ftp.cixug.es/apache/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz`

`tar xvf spark-3.1.2-bin-hadoop3.2.tgz`

`sudo mv spark-3.1.2-bin-hadoop3.2 /usr/local/spark`

`nano ~/.profile` (añadir en la última linea: PATH="$PATH:/usr/local/spark/bin")

`source ~/.profile`

* Instalar git y pip3: `sudo apt install git` , `sudo apt install pip3`

`git clone <url repo>`

`cd <your-project>`

* Crear y activar un entorno virtual

`pip install venv`
    
`python3 -m venv env`
    
`source env/bin/activate`
_________________________
    
`pip3 install --upgrade pip`

`pip3 install wheel`

`pip3 install google-cloud-storage`

* Instalar los paquetes requeridos para ejecutar el proyecto:
    
`pip3 install -r requirements.txt`


## Contenido del proyecto

FALTA


## Pasos adicionales para implementar el código en un Cluster de Google Cloud
Abrir una Cloud Shell en la página de google cloud
- crear un clúster nuevo: $ gcloud dataproc clusters create example-cluster --enable-component-gateway --region europe-west6 --zone europe-west6-b --master-machine-type n1-standard-4 --master-boot-disk-size 50 --num-workers 2 --worker-machine-type n1-standard-4 --worker-boot-size-disk 50 --image-version 2.0-debian10
- Una vez creado el cluster acceder a la máquina principal por SSH y ejecutar los siguientes comandos (para obtener información más detallada acceder a https://cloud.google.com/architecture/chrome-desktop-remote-on-compute-engine)
    - Actualizar datos de apt e instalar wget y tasksel:
        - $ sudo apt update
        - $ sudo apt install --assume-yes wget tasksel
    - Descargar e instalar el paquete de instalación del escritorio remoto de Chrome para Debian:
        - $ wget https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb
        - $ sudo apt-get install --assume-yes ./chrome-remote-desktop_current_amd64.deb
    - Instalar en entorno de escritorio Xfce (los otros entornos no funcionan, da error de paquetes rotos al intentar instalarlos):
        - $ sudo DEBIAN_FRONTEND=noninteractive \ apt install --assume-yes xfce4 desktop-base dbus-x11 xscreensaver
    - Configurar el escritorio remoto de Chrome para ejecutar Xfce de forma predeterminada:
        - $ sudo bash -c 'echo "exec /etc/X11/Xsession /usr/bin/xfce4-session" > /etc/chrome-remote-desktop-session'
    - Inhabilitar el servicio de administrador de pantallas de la instancia actual
        - $ sudo systemctl disable lightdm.service
    - Instalar Google Chrome en la instancia   
        - $ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
        - $ sudo apt install --assume-yes ./google-chrome-stable_current_amd64.deb
- En el navegador Chrome de la MÁQUINA LOCAL, acceder a la página de configuración de la línea de comandos del escritorio remoto de Chrome
    - https://remotedesktop.google.com/headless
    - Hacer clic en configurar otra computadora y Comenzar
    - Descargar e instalar el Chrome Remote Desktop y pulsar en Siguiente
    - Hacer Clic en Autorizar
    - Copiar y pegar las líneas de comandos equivalentes a Debian en la MÁQUINA MAESTRA DEL CLUSTER
    - Introducir un Pin de 6 dígitos para acceder al clúster remotamente
- Confirmar que el servicio de escritorio remoto está en ejecución:
    - $ sudo systemctl status chrome-remote-desktop@$USER

## Más Información
    
Se puede encontrar más información referente a nuestro proyecto en nuestra página web:
    https://big-data-analytics-ucm.github.io/Youtube-Trending-Videos-Analysis/# 
    
O en el github:
    https://github.com/Big-Data-Analytics-UCM/Youtube-Trending-Videos-Analysis 
    
Los datasets utilizados para el análisis pueden ser descargados desde el siguiente enlace:
    [YoutubeAnalisis.csv](https://www.kaggle.com/rsrishav/youtube-trending-video-dataset) 
    
    
    Este proyecto ha sido desarrollado por:
        * Lluc Bonet Seguí
        * Álvaro Plaza Sanz
        * Marcos Matute Fernández
        * Sergio Crespillo Campos
        * Camilo Andres D’isidoro

    
    
