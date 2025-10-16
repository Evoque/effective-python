import time
from threading import Thread
from queue import Queue, ShutDown

class StoppableWorker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue 
        
    def run(self):
        while True:
            try:
                item = self.in_queue.get()
            except ShutDown:
                break
            else:
                result = self.func(item)
                self.out_queue.put(result)
                self.in_queue.task_done()

def start_threads(count, *args):
    threads = [StoppableWorker(*args) for _ in range(count)]
    for thread in threads:
        thread.start()
    return threads


def download(item):
    return item

def resize(item):
    return item

def upload(item):
    return item  

download_queue = Queue()
resize_queue = Queue(100)
upload_queue = Queue(100)
done_queue = Queue()

threads = (
    start_threads(3, download, download_queue, resize_queue)
    + start_threads(4, resize, resize_queue, upload_queue)
    + start_threads(5, upload, upload_queue, done_queue)
)

start = time.perf_counter()

for _ in range(2000):
    download_queue.put(object())

download_queue.shutdown()
download_queue.join()

resize_queue.shutdown()
resize_queue.join()

upload_queue.shutdown()
upload_queue.join()

'''
神奇配合: shutdown(), task_done(), join()
'''
def drain_queue(input_queue):
    input_queue.shutdown()
    counter = 0
    
    while True:
        try:
            input_queue.get()
        except ShutDown:
            break
        else:
            input_queue.task_done()
            counter += 1
    
    input_queue.join()
    return counter 

counter = drain_queue(done_queue)

for t in threads:
    t.join()

end = time.perf_counter()
delta = end - start 
print(counter, "items finished! - ", f"{ delta: .5f} second")
