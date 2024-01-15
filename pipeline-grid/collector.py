import zmq
import logging

logging.basicConfig(level=logging.INFO)
context = zmq.Context()
sock = context.socket(zmq.PULL)
sock.bind("tcp://127.0.0.1:8889")

while True:
    task = sock.recv_json()
    logging.info(
        f"[collector] {task.get("worker", "unknown")} -> {task.get("result", "invalid")}"
    )
