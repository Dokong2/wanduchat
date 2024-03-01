import server, client

print("완두챗 - 릴리즈 1.0")
print("서버 생성은 [server] 입력")
print("클라이언트로 서버 접속은 [client] 입력")
while True:
    starting = input(">>")
    if starting == "server":
        print("서버 생성중..")
        server.start()
    elif starting == "client":
        print("서버 접속중..")
        client.start()
    else:
        print("잘못된 명령입니다. 다시 입력해주세요.")
        print(f"입력하신 명령어 : {starting}")