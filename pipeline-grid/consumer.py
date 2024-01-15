import zmq
import logging
import sys

logging.basicConfig(level=logging.INFO)
context = zmq.Context()
from_producer = context.socket(zmq.PULL)
from_producer.connect("tcp://127.0.0.1:8888")
to_collector = context.socket(zmq.PUSH)
to_collector.connect("tcp://127.0.0.1:8889")

if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    logging.error("missing consumer name")
    sys.exit()

while True:
    task = from_producer.recv_json()
    task["worker"] = name
    logging.info(f"[consumer] got {task}")
    action = task.get("action", None)
    params = [int(task[key]) for key in task.keys() if key.startswith("p")]
    match action:
        case "SUM":
            result = sum(params)
            task["result"] = result
            logging.info(f"\t[consumer] computed {result}")
            to_collector.send_json(task)
        case _:
            logging.warn(f"invalid action {action}")
