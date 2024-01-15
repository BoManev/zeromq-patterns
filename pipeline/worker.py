import zmq

context = zmq.Context()
sock = context.socket(zmq.PULL)
sock.connect("tcp://127.0.0.1:8888")

while True:
    message = sock.recv_string()
    print(message)
