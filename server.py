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

def clientbangsong(data):
    global connlist
    for conn in connlist:
        conn.send(data.encode())

if __name__ == "__main__":
    start()