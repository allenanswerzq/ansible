from __future__ import annotations

import contextlib
import os
import typing as t

if os.name == 'nt':
    import msvcrt
else:
    import fcntl


@contextlib.contextmanager
def named_mutex(path: str) -> t.Iterator[None]:
    """
    Lightweight context manager wrapper over `fcntl.flock` to provide IPC locking via a shared filename.
    Entering the context manager blocks until the lock is acquired.
    The lock file will be created automatically, but creation of the parent directory and deletion of the lockfile are the caller's responsibility.
    """
    with open(path, 'a+b') as file:
        if os.name == 'nt':
            file.seek(0, os.SEEK_END)
            if file.tell() == 0:
                file.write(b'\0')
                file.flush()
            file.seek(0)
            msvcrt.locking(file.fileno(), msvcrt.LK_LOCK, 1)
        else:
            fcntl.flock(file, fcntl.LOCK_EX)

        try:
            yield
        finally:
            if os.name == 'nt':
                file.seek(0)
                msvcrt.locking(file.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(file, fcntl.LOCK_UN)
