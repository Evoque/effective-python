import time

def factorize(number):
    # print(f" ----> factorizing {number}")
    for i in range(1, number + 1):
        if number % i == 0:
            yield i
            
numbers = [7775876, 6694411, 5038540, 5426782,
           9934740, 9168996, 5271226, 8288002,
           9403196, 6678888, 6776096, 9582542,
           7107467, 9633726, 5747908, 7613918]
# Serial
start = time.perf_counter()
for number in numbers:
    list(factorize(number))
end = time.perf_counter()
delta = end - start
print(f"Serial takes {delta: .5f} seconds!")

# MultiThreading
from threading import Thread

class FactorizeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number 
        
    def run(self):
        self.factors = list(factorize(self.number))
        
tstart = time.perf_counter()
threads = []
for n in numbers:
    thread = FactorizeThread(n)
    thread.start()
    threads.append(thread)
    
for t in threads:
    t.join()

tdelta = time.perf_counter() - tstart
print(f"Threading takes {tdelta: .5f} seconds!")

