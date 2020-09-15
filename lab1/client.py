import socket

with socket.socket() as sock:
    sock.connect(("127.0.0.1", 10001))
    sock.sendall("ping".encode("utf8"))
