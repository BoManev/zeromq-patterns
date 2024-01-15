import zmq

context = zmq.Context()
sock = context.socket(zmq.PAIR)
sock.connect("tcp://127.0.0.1:8888")

sock.send_string("a message")
print(f"echo: {sock.recv_string()}")
