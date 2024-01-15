import zmq
import time

context = zmq.Context()
# fire&forget socket
sock = context.socket(zmq.PUB)
sock.bind("tcp://127.0.0.1:8888")

id = 0

while True:
    time.sleep(1)
    id, now = id + 1, time.ctime()
    sock.send_string("{topic} [pub] {id} at {now}".format(topic=1, id=id, now=now))
    sock.send_string("{topic} [pub] {id} at {now}".format(topic=2, id=id, now=now))
