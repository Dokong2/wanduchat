import socket, threading
server = None

def giveserver(data):
    global server
    server.send(data.encode())

def chating(name):
    global server
    while True:
        chatdata = input("")
        giveserver(name + " : " + chatdata)

def start():
    global server
    host = socket.gethostname()
    server = socket.socket()
    print("이름을 입력하세요.")
    name = input(">>")
    server.connect((host, 1010))
    print("서버에 접속을 성공했습니다.")
    threading.Thread(target=chating, args=[name,]).start()
    threading.Thread(target=printmsg).start()

def printmsg():
    global server
    while True:
        msg = server.recv(1024).decode()
        print(msg)

if __name__ == "__main__":
    start()