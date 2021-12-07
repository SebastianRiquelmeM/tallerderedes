def loss(packet):
    import time
    import random
    import ast
    t = float(time.time())
    if not hasattr(packet, 'ult'):
        packet.global_var('ult', t)
    if not hasattr(packet, 'perdida'):
        packet.global_var('perdida', 0)
    if not hasattr(packet, 'gp'):
        packet.global_var('gp', 0)
    if not hasattr(packet, 'thr'):
        packet.global_var('thr', 0)
    delta = t- packet.ult

    if delta >= 1:
        tasa_perdida = packet.perdida
        goodput = packet.gp
        throughput = packet.thr
        print("lost: " + str(tasa_perdida) + " -throughput " + str(throughput) + "Byte/s - goodput " + str(goodput) + "Byte/s ")
        packet.ult = float(time.time())
        packet.gp = 0
        packet.thr = 0
        packet.lat = 0
    n = random.randint(0,9)
    """
    if n<=2:
        packet.perdida = packet.perdida + 1
        packet['IP']['addr'] = "172.17.0.0"
    """

    largo = ast.literal_eval(packet['TCP']['len'].replace("x0", ""))
    packet.gp = packet.gp + largo
    packet.thr = packet.thr + packet["IP"]["len"] + largo
    return packet
