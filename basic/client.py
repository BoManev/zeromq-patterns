import zmq
import sys

context = zmq.Context()
sock = context.socket(zmq.REQ)
sock.connect("tcp://127.0.0.1:8888")

sock.send_string(" ".join(sys.argv[1:]))
print(f"[client] {sock.recv_string()}")
