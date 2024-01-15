import zmq
import logging

logging.basicConfig(level=logging.INFO)

try:
    context = zmq.Context()
    s_from = context.socket(zmq.XREP)
    s_from.bind("tcp://127.0.0.1:8888")
    s_to = context.socket(zmq.XREQ)
    s_to.bind("tcp://127.0.0.1:8889")
    zmq.device(zmq.QUEUE, s_from, s_to)
except Exception as e:
    logging.exception(e)
finally:
    # s_from.close()
    # s_to.close()
    # context.term()
    context.destroy()
