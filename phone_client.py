import socket
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(("127.0.0.1", 8086))


while True:
    try:
        msg = input(">>: ").strip()
        phone.send(msg.encode("utf-8"))
        data = phone.recv(1024)
        print("服务端返回的数据：", data.decode("utf-8"))
    except:
        break
print("phone connection close.")
phone.close()