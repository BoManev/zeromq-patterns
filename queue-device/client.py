import zmq
import time
import logging

logging.basicConfig(level=logging.INFO)

context = zmq.Context()
sock = context.socket(zmq.REQ)
sock.connect("tcp://127.0.0.1:8888")

i = 0
while True:
    i += 1
    sock.send_string(f"[client] message ID: {i}")
    logging.info(f"[client] got {sock.recv_string()}")
    time.sleep(1)
