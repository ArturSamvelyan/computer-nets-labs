import socket


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind(("127.0.0.1", 10001))
    while True:
        (msg, addr) = sock.recvfrom(1024)
        print("Msg: " + msg.decode("utf8"))
        print("Addr: ", addr)
