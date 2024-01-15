import zmq

context = zmq.Context()
sock = context.socket(zmq.REP)
sock.bind("tcp://127.0.0.1:8888")

while True:
    message = sock.recv_string()
    print(f"[server] got {message}")
    sock.send_string(f"[server] echo: {message}")
    