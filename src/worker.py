from hotqueue import HotQueue
import os
import sys
try:
    REDIS_IP = os.environ['REDIS_IP']
except KeyError:
    print("REDIS_IP is required")
    sys.exit(1)

q = HotQueue('queue', host=REDIS_IP, port=6379, db=1)

@q.worker

def do_work(item):
    print(item)

do_work() 
