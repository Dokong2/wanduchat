import socket, threading
connlist = []
connlist2 = []

def start():
    global connlist, connlist2
    host = socket.gethostname()
    server = socket.socket()
    server.bind((host, 1010))
    bangsong = socket.socket()
    bangsong.bind((host, 2020))
    print("서버 생성이 완료되었습니다.")
    print("클라이언트 대기를 시작합니다.")
    server.listen(2)
    while True:
        conn, addr = server.accept()
        connlist.append(conn)
        print("클라이언트가 접속했습니다.")
        print(f"콘 : {conn}")
        print(f"어드레스 : {addr}")
        clientbangsong(f"클라이언트가 접속했습니다. 콘 : {conn}, 어드레스 : {addr}")
        giveingdatasend(conn=conn)

def giveingdatasend(conn):
    while True:
        bangsongdata = conn.recv(1024).decode()
        bangsongdata = str(bangsongdata)
        clientbangsong(bangsongdata)
        print(f"방송서버에 데이터가 와 클라이언트에게 전송합니다.. 받은 데이터 : {bangsongdata}")

def clientbangsong(data):
    global connlist2
    for conn in connlist2:
        conn.send(data.encode())
    print(f"모든 클라이언트에게 메시지 [{data}]가 전송되었습니다.")

if __name__ == "__main__":
    start()