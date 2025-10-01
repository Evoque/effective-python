
import os
import sys
import time

r_fd, w_fd = os.pipe()

while True:
    print('*' * 20)
    print(f'parent pid: {os.getpid()}')
    print(f'r_fd: {r_fd}')
    print(f'w_fd: {w_fd}')
    print('*' * 20)
    time.sleep(10)

# pid = os.fork()

# if pid > 0:
#     while True:
#         print('*' * 20)
#         print(f'parent pid: {os.getpid()}')
#         print(f'r_fd: {r_fd}')
#         print(f'w_fd: {w_fd}')
#         print('*' * 20)
#         time.sleep(10)
# else: 
#     while True:
#         print('*' * 20)
#         print(f'child pid: {os.getpid()}')
#         print(f'r_fd: {r_fd}')
#         print(f'w_fd: {w_fd}')
#         print('*' * 20)
#         time.sleep(10)


    