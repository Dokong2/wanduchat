import socket, threading
server = None

def giveserver(data):
    global server
    server.send(data.encode())

def start():
    global server
    host = socket.gethostname()
    server = socket.socket()
    print("이름을 입력하세요.")
    name = input(">>")
    try:
        server.bind((host, 1010))
        print("서버에 접속을 성공했습니다.")
        threading.Thread(target=chating, args=name)
    except:
        print("서버 접속에 실패했습니다. 서버가 켜저 있는지 확인하세요.")

def printmsg():
    global server
    while True:
        msg = server.recv(1024).decode()
        print(msg)

def chating(name):
    global server
    while True:
        chatdata = input(f"{name}>>")
        giveserver(name + " : " + chatdata)