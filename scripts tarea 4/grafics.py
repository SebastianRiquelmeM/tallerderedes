import csv
import matplotlib.pyplot as plt

nombre_archivo = "E:\\Users\\Administrador\\Desktop\\sindelay.csv"
with open(nombre_archivo, "r") as archivo:
    lector = csv.reader(archivo, delimiter=",")
    # Omitir el encabezado
    next(lector, None)

    cont = 0
    conteo = []

    tiempo = 0

    # Para duplicación de paquetes
    dup = 0

    # Para Delay
    a = 0
    b = 0
    cant_paquetes = 0
    suma = 0
    origen = "172.17.0.3"

    # Para throughput
    thr = 0


    duplicado = []
    delay = []
    throughput = []

    for fila in lector:
        
        ip = fila[2]

        while tiempo + 1 < float(fila[1]):
            cont = cont + 1
            conteo.append(cont)

            while tiempo + 1 < float(fila[1]):
                tiempo = tiempo + 1

            # Guardar duplicados a cada segundo
            duplicado.append(dup)
            dup = 0

            # Guardar delay a cada segundo
            if(cant_paquetes == 0):
                delay.append(0)
            else:
                delay.append(suma/cant_paquetes)
            suma = 0
            cant_paquetes = 0

            # Throughput
            throughput.append(thr)
            thr = 0

        if "Dup" in fila[6] or "Retransmission" in fila[6]:
            dup = dup + 1
        elif origen != ip:
            b = float(fila[1])
            suma = suma + b-a
            cant_paquetes = cant_paquetes + 1
        else:
            a = float(fila[1])
            origen = ip

        thr = thr + int(fila[5])

    cont = cont + 1
    conteo.append(cont)

    duplicado.append(dup)
    throughput.append(thr)
    if(cant_paquetes == 0):
        delay.append(0)
    else:
        delay.append(suma/cant_paquetes)


    # Delay
    plt.plot(conteo, delay)
    plt.xlabel("Tiempo en la captura")
    plt.ylabel("Delay")
    plt.show()

    #Paquetes duplicados
    plt.figure(2)
    plt.plot(conteo, duplicado)
    plt.xlabel("Tiempo en la captura")
    plt.ylabel("Paquetes duplicados")
    plt.show()

    #Throughput
    plt.figure(3)
    plt.plot(conteo, throughput)
    plt.xlabel("Tiempo en la captura")
    plt.ylabel("Throughput")
    plt.show()
