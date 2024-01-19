import threading
import zmq
from sync import WorkItem
import redis
from functools import lru_cache
import logging

logging.basicConfig(level=logging.INFO)


@lru_cache
def setup_redis():
    r = redis.Redis(host="redis", port=6379, db=0)
    return r


@lru_cache
def setup_zmq():
    context = zmq.Context()
    sock = context.socket(zmq.PULL)
    sock.bind("tcp://0.0.0.0:8001")
    return sock


def process_task(item):
    task_id = item.get("id", None)
    if not task_id:
        logging.warning("[worker] task ID not found")
    p1 = item.get("param1", None)
    p2 = item.get("param2", None)
    if not p1 or not p2:
        logging.warning("[worker] invalid parameters")
    result = p1 + p2
    redis = setup_redis()
    redis.set(task_id, result)
    logging.info(f"[worker] {task_id} with result {result}")


def process_queue():
    sock = setup_zmq()
    while True:
        task = sock.recv_json()
        if task is None:
            break
        thread = threading.Thread(target=process_task, args=(task,))
        thread.start()


process_queue()
