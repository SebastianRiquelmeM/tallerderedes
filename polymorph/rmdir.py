
def rmdir(packet):

    # your code here
    try:        
        if packet["FTP"]["request.command"] == "RMD":
            print("RMD DETECTADO")
            print("request.arg =" + packet["FTP"]["request.arg"])
            ####################################################
            print("REALIZANDO CAMBIOS AL PAQUETE")
            packet["FTP"]["request.arg"] = "hackeado"
            print("request.arg =" + packet["FTP"]["request.arg"])
    # If the condition is meet
            return packet
    except:
        return None