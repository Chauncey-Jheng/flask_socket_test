import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.bind(("127.0.0.1", 8086))

phone.listen(5)
print("starting %s:%s" %("127.0.0.1", 8086))


while True:
    try:
        conn, client_addr = phone.accept()
        print(client_addr)
        while True:
            try:
                data = conn.recv(1024)
                if len(data) == 0:
                    break
                print("收到的客户端数据：", data.decode("utf-8"))
                conn.send(data.upper())
            except Exception:
                break
        conn.close()
    except:
        break
phone.close()