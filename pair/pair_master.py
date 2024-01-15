import zmq

context = zmq.Context()
sock = context.socket(zmq.PAIR)
sock.bind("tcp://127.0.0.1:8888")

message = sock.recv_string()
sock.send_string(f"[echo] {message}")
