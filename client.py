import socket
import time
import random

address = ('192.168.0.172', 31500)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = 'hello, world!'
    for i in range(20):
        t=random.randint(1, 5)
        s.sendto('['+str(i)+']'+msg, address)
        print(str(t)+'['+str(i)+']')
        time.sleep(t)
    break

s.close()
