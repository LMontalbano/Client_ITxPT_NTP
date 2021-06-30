import socket

TCP_IP = "192.168.0.10"
TCP_PORT = 9000

BUFFER_SIZE = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((TCP_IP, TCP_PORT))
data = s.recv(BUFFER_SIZE)
s.close()

print("received data:", data)