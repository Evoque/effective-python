'''
@TODO: 用3.14, 关闭GIL再测试一遍！
'''
import select
import socket
from threading import Thread, Event, Lock
import time

all_tasks_done = Event()
completed_count = 0
counter_lock = Lock()

def slow_system_call():
    select.select([socket.socket()], [], [], 2)

class FactorizeThread(Thread):
    def __init__(self, counter_lock):
        super().__init__()
        self.counter_lock = counter_lock
        
    def run(self):
        global completed_count
        with self.counter_lock:
            print(f"子线程 {completed_count} 完成了任务")
            completed_count += 1
            if completed_count == 5:
                all_tasks_done.set()
                
        slow_system_call()
        

threads = []
for i in range(5):
    thread = FactorizeThread(counter_lock)
    thread.start()
    threads.append(thread)
    
while not all_tasks_done.is_set():
    print(f"主线程开始闹着玩 -- {completed_count}")
    time.sleep(0.5)
    
print("while 结束了！！！！！！！！")