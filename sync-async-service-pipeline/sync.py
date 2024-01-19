from fastapi import FastAPI
from functools import lru_cache
import zmq
from pydantic import BaseModel
import uuid
import redis
import socket

app = FastAPI()


@lru_cache
def setup_redis():
    r = redis.Redis(host="redis", port=6379, db=0)
    return r


@lru_cache
def setup_zmq():
    context = zmq.Context()
    sock = context.socket(zmq.PUSH)
    sync_ip = socket.gethostbyname("async")
    sock.connect(f"tcp://{sync_ip}:8001")
    return sock


class WorkItem(BaseModel):
    param1: int
    param2: int


@app.post("/data")
def post_task(work: WorkItem):
    sock = setup_zmq()
    task = work.model_dump()
    task_id = uuid.uuid4()
    task["id"] = str(task_id)
    sock.send_json(task)
    return {"id": task_id}


@app.get("/data")
def read_task(id: uuid.UUID):
    redis = setup_redis()
    result = redis.get(str(id))
    return {"task_result": result}
