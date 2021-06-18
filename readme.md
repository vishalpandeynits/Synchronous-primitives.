## Synchronous primitives

There are few problem with multithreading module that if many threads try
to access the same piece of data can lead to problems like making data inconsistent or 
getting garbled output (like having `HWeolrldo` in place of `Hello World` on your console). 
Such problems can arise when we don’t tell the computer how to mange threads in an 
organized manner. We can tell our computer to work in harmonious manner using
`synchronous primitives`.

`synchronization primitives` are simple software mechanisms to ensure that our threads
run in a harmonious manner with each other. They methods which block execution of a 
particular thread until some condition is met.

Main `synchronous primitives` are:
1. Locks
2. RLocks
3. Semaphores
4. Events
5. Conditions 
6. Barriers

We can also create our custom `synchronous primitives` by inheriting these synchronous primitives.