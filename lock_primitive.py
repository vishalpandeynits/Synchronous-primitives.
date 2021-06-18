# Locks are the simplest synchronization primitives in Python.  
# A Lock has only two  states — locked and unlocked. 
# It is created in the unlocked state and has two principal methods — acquire() and release().

# The acquire() method locks the Lock and blocks execution until the 
# release() method in some other coroutine sets it to unlocked.

# The release() method should only be called in the locked state, 
# it sets the state to unlocked and returns immediately. 
# If release() is called in the unlocked state, a RunTimeError is raised.

from threading import Lock, Thread
lock = Lock()
g = 0

def add_one():
   global g
   lock.acquire()
   g += 1
   lock.release()

def add_two():
   global g
   lock.acquire()
   g += 2
   lock.release()

threads = []

for func in [add_one, add_two]:
   threads.append(Thread(target=func))
   threads[-1].start()

for thread in threads:
   """
   Waits for threads to complete before moving on with the main
   script.
   """
   thread.join()

print(g)