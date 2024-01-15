import zmq
import time

context = zmq.Context()
sock = context.socket(zmq.PUSH)
sock.bind("tcp://127.0.0.1:8888")

id = 0

while True:
    id, now = id + 1, time.ctime()
    sock.send_string(f"{id} at {now}")
    time.sleep(1)
