import socket


addr_port = ("127.0.0.1", 10001)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.sendto("hello world".encode("utf8"), addr_port)
