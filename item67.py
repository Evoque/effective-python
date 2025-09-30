

# import subprocess

# result = subprocess.run(
#     ["echo", "Hello from the child!"],
#     capture_output=True,
#     encoding="utf-8",
# )

# result.check_returncode() # No exception means it exited cleanly

# print(result.stdout)


''' Decoupling the child process from the parent frees up the parent process to run many child processes in parallel. '''
# import time
# import subprocess 

# start = time.perf_counter()
# sleep_procs = []
# for _ in range(10):
#     proc = subprocess.Popen(["sleep", "1"])
#     sleep_procs.append(proc)
    
# for proc in sleep_procs:
#     proc.communicate()

# end = time.perf_counter()
# delta = end - start
# print(f"Finished in {delta:.10} seconds")

import os
import subprocess

def run_encrypt(data):
    env = os.environ.copy()
    env["password"] = "zf7ShyBhZOraQDdE/FiZpm/m/8f9X+M1"
    proc = subprocess.Popen(
        ["openssl", "enc", "-pbkdf2", "-pass", "env:password"],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    proc.stdin.write(data)
    proc.stdin.flush()  
    return proc

def run_hash(input_stdin):
    return subprocess.Popen(
        ["openssl", "dgst", "-sha256", "-binary"],
        stdin=input_stdin,
        stdout=subprocess.PIPE,
    )
    
encrypt_procs = []
hash_procs = []

for _ in range(3):
    data = os.urandom(10)
    
    encrypt_proc = run_encrypt(data)
    encrypt_procs.append(encrypt_proc)
    
    # aa = encrypt_proc.stdout.fileno()
    # print(f'aa: {aa}')
    time.sleep(1)
    encrypt_proc.stdout.close()
    encrypt_proc.stdout = None
    
    
    # hash_proc = run_hash(encrypt_proc.stdout)
    # hash_procs.append(hash_proc)
     

    
import os
import time 

for proc in encrypt_procs:
    res,_ = proc.communicate()
    print(f'res: {res}')
    assert proc.returncode == 0
    
# for proc in hash_procs:
#     out, _ = proc.communicate()
#     print(out[-10:])
#     assert proc.returncode == 0

# while True:
#     print("*" * 20)
#     print(f"PID {os.getpid()} ")
#     for proc in encrypt_procs:
#         print(f"encrypt-PID {proc.pid} ")
    
#     # for proc in hash_procs:
#     #     print(f"hash-PID {proc.pid} ")
    
#     print("*" * 20)
#     time.sleep(20)
