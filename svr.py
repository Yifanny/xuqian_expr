import socket
import time
from multiprocessing import Process, Queue, Lock

def receive(queue, lock, t):
    time.sleep(t)
    lock.acquire()
    print queue.get()
    lock.release()

address = ('192.168.0.172', 31500)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)
rec_data = []
buff = Queue(2048)
lock = Lock()

while True:
    data, addr = s.recvfrom(2048)
    buff.put(data)
    if not data:
        print "client has exist"
        break
    Process(target = receive, args = (buff, lock, 3)).start()

s.close()
