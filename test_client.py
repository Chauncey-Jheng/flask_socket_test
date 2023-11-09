import socket
import json
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(("127.0.0.1", 8086))


while True:
    try:
        data = phone.recv(1024)
        msg = data.decode("utf-8")
        print("服务端返回的数据：", msg)
        msg = json.loads(msg)
        video_file_path = msg["video_file_path"] 
        ocr_file_path = msg["ocr_file_path"]
        asr_file_path = msg["asr_file_path"]
        print("video_file_path is", video_file_path)
        print("ocr_file_path is", ocr_file_path)
        print("asr_file_path is", asr_file_path)
    except:
        break
print("phone connection close.")
phone.close()