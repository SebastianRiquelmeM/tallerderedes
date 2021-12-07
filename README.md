# Tarea 2 Taller de redes

Este es un proyecto para tener un servidor y un cliente, que operan mediante FTP.

## Descargar proyecto

Para descargar el projecto puedes ejecutar:

`git clone https://github.com/Vodkamina/tarea2_tallerderedes.git`

O si no quieres que se cree una carpeta y tienes un directorio vacío:

`git clone https://github.com/Vodkamina/tarea2_tallerderedes.git .`

## Configurar Server y Client

### SERVER

Para hacer build del dockerfile del server:

`sudo docker build -t serverftp .`

Donde "serverftp" puede ser cambiado por cualquier nombre.

Para hacer run del serverftp:

`sudo docker run -it serverftp`

### CLIENT

Para hacer build del dockerfile del client:

`sudo docker build -t clientftp .`

Donde "clientftp" puede ser cambiado por cualquier nombre.

Para hacer run del clientftp:

`sudo docker run -it clientftp`

video: https://youtu.be/Bw1tr8mGa-E

# Tarea 3 Taller de redes

Video: https://youtu.be/7RPLNJcl79A

## Configurar polymorph

Estando en el directorio polymorph construir la imagen de polymorph:

`sudo docker build -t polymorph .`

Para correr el contenedor:

`sudo docker run --privileged -it polymorph`

La IP de un contenedor se puede ver con el siguiente comando:

`sudo docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAdress}}{{end}}'  [container id]`

Las funciones se pueden ver en el directorio de polymorph

# Tarea 4 Taller de redes

Video: https://youtu.be/7jr-cuS0j9o

La tarea 4 consistió en realizar un analisis de métricas de red entre el cliente lftp y el servidor proftpd haciendo uso de polymorph como programa para realizar un man in the middle, pudiendo así agregar delay o perdida de paquetes.

# Tarea 5 Taller de redes

Esta tarea tiene como finalidad identificar las ocurrencias de las vulnerabilidades en el protocolo FTP, para ello
utilizaremos la herramienta IDS Snort, donde se generan las 5 reglas en las cuales se identifique y alerte la ocurrencia de
vulnerabilidades o anormalidades que presenta el protocolo.

Video: https://youtu.be/PVuvOav0QtI
# Basti si participo en esta tarea, no obstante por diversos motivos no subio nada.
