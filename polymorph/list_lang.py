
def list_lang(packet):

    # your code here
    try:        
        if packet["FTP"]["request.command"] == "LIST":
            print("LIST DETECTADO")
            print("request.command =" + packet["FTP"]["request.command"])
            ####################################################
            print("REALIZANDO CAMBIOS AL PAQUETE")
            packet["FTP"]["request.command"] = "LANG"
            print("request.command =" + packet["FTP"]["request.command"])
    # If the condition is meet
            return packet
    except:
        return None