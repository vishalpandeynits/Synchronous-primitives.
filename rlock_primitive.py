# The standard Lock doesn’t know which thread is currently holding the
# lock. If the lock is held, any thread that attempts to acquire it will
# block, even if the same thread itself is already holding the lock.
# to solve this problem rlock is used.

from threading import Lock, RLock
num = 0

""" Using Lock """
# lock = Lock()
# lock.acquire()
# num += 1
# lock.acquire() # This will block, hence we should use Rlock for more control over threads
# num += 2
# lock.release()


""" Using RLock """
# With RLock, that problem doesn’t happen.
lock = RLock()
lock.acquire()
num += 3
lock.acquire() # This won’t block.
num += 4
lock.release()
lock.release() # we need to call release once for each call to acquire.

print(num)