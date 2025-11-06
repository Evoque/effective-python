

from collections import deque 
from queue import Queue
from threading import Thread


my_queue = Queue()
def consumer():
    print("Consumer waiting")
    my_queue.get()
    print("Consumer done")
    
thread = Thread(target=consumer)
thread.start()

print("Producer putting")
my_queue.put(object())
print("Producer done")

thread.join()




    
    
