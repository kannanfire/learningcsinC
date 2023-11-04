import time
import os
import sys

# print(f"pid: {os.getpid()}")

with open('/var/tmp/file1.db', 'r') as f:
    print(f.fileno())

    pid = os.fork()

    if not pid:
        print(f"pid: {os.getpid()}")
        f.seek(int(sys.argv[1]))
        time.sleep(9999)

    os.waitpid(pid, 0)