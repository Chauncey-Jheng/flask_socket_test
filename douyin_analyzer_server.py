import socket
import time
import json

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ss.bind(("127.0.0.1", 8086))

ss.listen(10)
print("starting %s:%s" %("127.0.0.1", 8086))

while True:
    try:
        conn, client_addr = ss.accept()
        print(client_addr)
        while True:
            try:
                rcv = conn.recv(1024)
                rcv = rcv.decode("utf-8")
                if rcv != "give_me_live_info":
                    raise Exception
                video_file_path = "balabala"
                asr_file_path = "balabala"
                ocr_file_path = "balabala"
                sendmsg = {"video_file_path":video_file_path,
                           "asr_file_path":asr_file_path,
                           "ocr_file_path":ocr_file_path}
                msg = json.dumps(sendmsg)
                data = msg.encode("utf-8")
                print("发送到客户端数据：", data)
                conn.send(data)
            except Exception:
                break
        conn.close()
    except:
        break
ss.close()