import zmq
import time
import logging

logging.basicConfig(level=logging.INFO)
context = zmq.Context()
sock = context.socket(zmq.PUSH)
sock.bind("tcp://127.0.0.1:8888")

i = 0
while True:
    i = i + 1
    message = {"action": "SUM", "p1": f"{i}", "p2": f"{i}"}
    sock.send_json(message)
    logging.info(f"[producer] {id} : {message!s}")
