


import subprocess

# result = subprocess.run(
#     ["echo", "Hello from the child!"],
#     capture_output=True,
#     encoding="utf-8",
# )

# # No exception means it exited cleanly
# result.check_returncode()

# print("*" * 20)
# print(f'result.stdout: {result.stdout}')
# print(f'result: {type(result)}')
# print(f'stdout: {type(result.stdout)}')
# print("*" * 20)



# proc = subprocess.Popen(["sleep", "1"])
# count = 0
# while (pp := proc.poll()) is None:
#     print(f'Working... {count}')
#     count += 1
    
# print(f'Exit, proc.poll(): {pp}') 
    

import os 

def run_encrypt(data):
    env = os.environ.copy()
    env["password"] = "zf7ShyBhZOraQDdE/FiZpm/m/8f9X+M1"
    proc = subprocess.Popen(
        ["openssl", "enc", "-des3", "-pass", "env:password"],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    proc.stdin.write(data)
    proc.stdin.flush() # Ensure that the child gets input
    return proc

def run_hash(input_stdin):
    return subprocess.Popen(
        ["openssl", "dgst", "-whirlpool", "-binary"],
        stdin=input_stdin,
        stdout=subprocess.PIPE,
    )

encrypt_procs = []
hash_procs = []
for _ in range(3):
    data = os.urandom(100)

    encrypt_proc = run_encrypt(data)
    encrypt_procs.append(encrypt_proc)

    hash_proc = run_hash(encrypt_proc.stdout)
    hash_procs.append(hash_proc)

    # Ensure that the child consumes the input stream and
    # the communicate() method doesn't inadvertently steal
    # input from the child. Also lets SIGPIPE propagate to
    # the upstream process if the downstream process dies.
    encrypt_proc.stdout.close()
    encrypt_proc.stdout = None
    
for proc in encrypt_procs:
    proc.communicate()
    assert proc.returncode == 0

for proc in hash_procs:
    out, _ = proc.communicate()
    print(out[-10:])
    assert proc.returncode == 0


proc = subprocess.Popen(["sleep", "10"])

try:
    proc.communicate(timeout=0.1)
except subprocess.TimeoutExpired:
    proc.terminate()
    proc.wait()
    
print(f'Exit status', proc.poll())


# Use the `run` convenience function for simple usage and the `Popen` class for advanced usage like 
# UNIX-style pipelines.