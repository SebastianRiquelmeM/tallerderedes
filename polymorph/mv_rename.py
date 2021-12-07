def mv_rename(packet):

    # your code here
    try:        
        if packet["FTP"]["request.command"] == "RNTO":
            print("RNTO DETECTADO")
            print("request.arg =" + packet["FTP"]["request.arg"])
            ####################################################
            print("REALIZANDO CAMBIOS AL PAQUETE")
            packet["FTP"]["request.arg"] = "hola hackeado.txt"
            print("request.arg =" + packet["FTP"]["request.arg"])
    # If the condition is meet
            print("SE RETORNA PAQUETE")
            return packet
    except:
        return None