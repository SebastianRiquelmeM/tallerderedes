def mkdir(packet):
    try:
        if packet["FTP"]["request.command"] == "MKD":
            print("MKD DETECTADO")
            print("request.arg =" + packet["FTP"]["request.arg"])
            ####################################################
            print("REALIZANDO CAMBIOS AL PAQUETE")
            packet["FTP"]["request.arg"] = "hackeado"
            print("request.arg =" + packet["FTP"]["request.arg"])
            print("SE RETORNA PAQUETE")
            return packet
    except:
        return None
    