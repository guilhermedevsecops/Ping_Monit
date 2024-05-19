import actions as act
import time
import socket

def ping_server(server: str, port: int, timeout=3):
    try:
        print("Novo")
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server, port))
    except OSError as error:
        return False
    else:
        s.close()
        return True
    

while True:
    print("Begin")
    a = ping_server("192.168.15.1", 5432)
    print("Condição")
    if(a == False):
        b = ping_server("192.168.15.1", 25)
        if(a == False and b == False):
            print("Aqui")
            act.catastrofe()
    else:
        print("Fim do programa")
        
    