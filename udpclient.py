import socket

target_host = "127.0.0.1"

target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("AAABBBCCC".encode(), (target_host, target_port))

data = "".format(client.recvfrom(4096))


print(data)
