def rm(packet):

    # your code here
    try:        
        if packet["FTP"]["request.command"] == "DELE":
            print("DELE DETECTADO")
            print("request.arg =" + packet["FTP"]["request.arg"])
            ####################################################
            print("REALIZANDO CAMBIOS AL PAQUETE")
            packet["FTP"]["request.arg"] = "hola.txt"
            print("request.arg =" + packet["FTP"]["request.arg"])
    # If the condition is meet
            print("SE RETORNA PAQUETE")
            return packet
    except:
        return None