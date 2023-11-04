#! /usr/bin/env python3

import os


with open('/var/tmp/file1.db', 'r') as f:
    print('fileno: ' + str(f.fileno()))

    print(f'parent: {os.getpid()}')
    os.dup2(f.fileno(), 123)

    pid = os.fork()

    if not pid:
        print(f'child: {os.getpid()}')
        # os.execve('./sleep.py', ['./sleep.py'], os.environ)

        maxfd = os.sysconf('SC_OPEN_MAX')

        os.closerange(3, maxfd)

        os.execve(os.getcwd() + "/sleep.py", ["./sleep.py"]  , os.environ)

        print('environ: ' + os.environ)

    f.seek(234)
    os.waitpid(-1, 0)