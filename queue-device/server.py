import zmq
import logging

logging.basicConfig(level=logging.INFO)

context = zmq.Context()
sock = context.socket(zmq.REP)
sock.connect("tcp://127.0.0.1:8889")

while True:
    message = sock.recv_string()
    logging.info(f"[server] got {message}")
    sock.send_string(f"[server] echo {message}")
