# Tarea 2 Taller de redes

Este es un projecto para tener un servidor y un cliente, que operan mediante FTP.

----------------------- SERVER -------------------------------

Para hacer build del dockerfile del server:

```sudo docker build -t serverftp .```

Donde "serverftp" puede ser cambiado por cualquier nombre.

Para hacer run del serverftp:

sudo docker run -it serverftp

----------------------- CLIENT --------------------------------

Para hacer build del dockerfile del client:

sudo docker build -t clientftp .

Para hacer run del clientftp:

sudo docker run -it clientftp

