Resources: CS 511 Slides and https://www.youtube.com/watch?v=ufdQ0GR855M

We have seen that semaphores are an efficient tool to solve synchronization problems.

However they have some **drawbacks:**

- They are low level constructs which means it is easy to forget an acquire or release or nest them incorrectly
- They are not related to the data which means they can appear in any part of the code

#### Monitor Definition

- Monitors are a high level abstraction that provides a convenient and effective mechanism for process synchronization
- Monitors give us a set of operations encapsulated in modules
- We have a unique lock that ensures mutual exclusion to all operations in the monitor
- Special variables called conidition variables are used to program conditional synchronization as well
- Monitors make synchronization easier by associating a lock directly with an object and its methods

#### Simple Monitor Example

```java
class Counter {
    private int counter = 0

    public synchronized void inc(){
        counter++
    }
    public synchronized void dec(){
        counter--
    }
}
Counter c = new Counter()

P = Thread.start{
    10.times{
        c.inc()
    }
}
Q = Thread.start{
    10.times{
        c.inc()
    }
}
P.join()
Q.join()
```

So what is the monitor actually doing here?

- A monitor is kind of like a room containing shared data with a door that can only be unlocked by one thread at a time
  - A thread must acquire the monitor's lock to enter
  - Only 1 thread can hold that lock
  - Other threads attempting to acquire it must wait
  - When a thread releases the lock, another thread can aquire it
  - In java every object has an associated instrinsic lock, aka a monitor loc

In the example above:

- When our methods have _synchronized_, java requires a thread to acquire the object's monitor lock before executing that method
- When the method is done, java releases the lock

The distinction with the above code and future codes are that the above code ensure just mutual exclusion. Only 1 thread can access the shared resource at at time.
Now, we will be looking at **condition synchronization** which allows a thread to wait until a particular condition becomes true using mechanisms like wait() and notify() and etc
We need to understand conditioning because our problems from before requires certain characteristics to be met. Like for reader/writer our readers needed to be 0 for them to let go of the semaphore.

#### Condition Variable Definition

Apart from the lock there are condition variables associated to the monitor.

- We can have built in ones called a **wait-set**
- And we can have user declared ones
  Monitors have operations that allow us to control the flow of threads:
- cond.wait()/await()
- cond.notify()/signal()
- cond.notifyAll()/signalAll()

**cond.wait()/await():**

- Always blocks the process and places it in the waiting set of the variable cond
- When it blocks it releases the mutex on the monitor

**cond.notify()/signal():**

- Unblocks the first process in the waiting set of the variable cond and sets it to the runnable states
- If there are no processes in the waiting set it has no effect

**cond.notifyAll()/signalAll():**

- Unblocks all the processes in the waiting set of the variable cond and sets them to the runnable state
- No effect if there are no processes in the waiting set

#### Condition Variables in Action

Let's work on the producer and consumer problem with condition variables and monitors.

Remember that this problem simply has a buffer. Producers write to it and consumers consume from it. They both edit the end index of the buffer. Consumers can only consume when a producer produced. There is a semaphore for both threads, and there is a mutex to edit the buffer.

```java
class Buffer {
    private Object buffer = null; // don't know why its not just a normal list...

    synchronized Object consume() {
        while (buffer == null)
            wait(); // wait on object's wait-set
        Object aux = buffer;
        buffer = null;
        notifyAll(); // signal on object's wait-set
        return aux;
    }

    synchronized void produce(Object o) {
        while (buffer != null)
            wait(); // wait on object's wait-set
        buffer = o;
        notifyAll(); // signal on object's wait-set
    }
}
```
