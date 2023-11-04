import os
import time

print(f"pid: {os.getpid()}")

fd1 = os.open('/var/tmp/file1.db', os.O_RDONLY, 777)

fd2 = os.dup(fd1)
fd3 = os.dup2(fd1, 999)

os.lseek(fd3, 100, 0)

time.sleep(180)