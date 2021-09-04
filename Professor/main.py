import socket
import threading


MESSAGE_LENGTH_HEADER_SIZE = 4
PORT = 5005

IP_ADDR = socket.gethostbyname(socket.gethostname())
ADDR = (IP_ADDR,PORT)

MESSAGE_FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = 'BYE'
print(IP_ADDR)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handleClient(conn:socket, addr):
    print("[*] New connection from http://{}:{}".format(addr[0],addr[1]))
    
    connected = True
    while(connected):
        message_length = conn.recv(MESSAGE_LENGTH_HEADER_SIZE).decode(MESSAGE_FORMAT)
        if message_length:
            message_length = int(message_length)
            message_content = conn.recv(message_length).decode(MESSAGE_FORMAT)
            if message_content == DISCONNECT_MESSAGE:
                connected = False
            print("[*] Message: {} from http://{}:{}".format(message_content, addr[0],addr[1]))
    
    print("[*] Diconnecting from http://{}:{}".format(addr[0],addr[1]))
    conn.close()

def run():
    server.listen()
    print("[*] Server started. Listening on http://{}:{}".format(IP_ADDR,PORT))
    while True:
        conn, add = server.accept()
        client_thread = threading.Thread(target=handleClient,args=(conn,add))
        client_thread.start()
        print("[*] Received a client connection")
        print("[*] TOTAL ACTIVE CONNECTIONS -> {}".format(threading.active_count()-1))

if __name__== "__main__":
    run()