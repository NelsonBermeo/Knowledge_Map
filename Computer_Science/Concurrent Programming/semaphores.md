We understand what Semaphores are in simple behavior patterns like producing regular expressions, but how are they used in famous concurrency problems?

## Problem 1 - Dining Philosophers

![alt text](/images/diningPhilosophersImage.png)

**Resources:** CS 511 Slides AND https://www.youtube.com/watch?v=FYUi-u7UWgw

**Problem Description:**

There are 5 philosophers and 5 forks. Philosophers can be in either state: thinking or eating. In order to eat a subject needs 2 forks.

The shared resources in this problem are the forks.

How can we let each philospher eat without deadlocks or starvation?

#### Naive Attempt

```java
final int N = 5
List<Semaphore> forks = []
N.times { forks.add(new Semaphore(1)) }
N.times {
    int id = it // in Groovy "it" is an iterator
    Thread.start {
        int left = id
        int right = (id + 1) % N
        println id + " Started " + left + ", " + right
        while (true) {
            // think
            println id + " Eating..."
            forks[left].acquire()
            forks[right].acquire()
            // eat
            forks[left].release()
            forks[right].release()
            println id + " Done Eating..."
        }
    }
}
```

This solution **deadlocks** because ...

#### Counting Semaphore

```java
final int N = 5
List<Semaphore> forks = []
N.times { forks.add(new Semaphore(1)) }
Semaphore chairs = new Semaphore(N - 1)
N.times {
    int id = it
    Thread.start {
        int left = id
        int right = (id + 1) % N
        println id + " Started " + left + "," + right
        while (true) {
            // think
            chairs.acquire() // Strong semaphore for starvation free
            forks[left].acquire()
            forks[right].acquire()
            println id + " Eating..."
            // eat
            forks[left].release()
            forks[right].release()
            println id + " Done Eating..."
            chairs.release()
        }
    }
}
```

I don't see a problem with this solution regarding deadlock, but could there be an issue with starvation? ...

#### Breaking the Symmetry

```java
final int N = 5
List<Semaphore> forks = []
N.times { forks.add(new Semaphore(1)) }
N.times {
    int id = it
    Thread.start {
        int left, right
        if (id == 0) {v // You won't be able to replay the bad situation because one of the philosophers won't grab the same fork. The different phil would be able to eat. It breaks that circular waiting.
            left = 1
            right = 0
        } else {
            left = id
            right = (id + 1) % N
        }
        println id + " Started " + left + "," + right
        while (true) {
            // think
            forks[left].acquire()
            forks[right].acquire()
            println id + " Eating..."
            // eat
            forks[left].release()
            forks[right].release()
            println id + " Done Eating..."
        }
    }
}
```

## Problem 2 - Producers/Consumers

![alt text](/images/producerConsumer.png)

**Resources:** CS 511 Slides

**Problem Description:**

The producer can work freely, the consumer must wait for the producer to produce and then consume.

The producer must wait when the buffer is full. The consumer must wait for the producer to produce.

There can be various producers and various consumers.

The shared resource is the buffer.

How can the producer and consumer do their jobs on the buffer without deadlock or starvation?

#### Split Binary Semaphores

This mimicks the behavior of printing "abababababab..." with semaphores. The producer goes, then the consumer goes. Just 1 consumer and 1 producer. It's like working with a buffer of size 1.

```java
Integer buffer;
Semaphore produce = new Semaphore(1);
Semaphore consume = new Semaphore(0);
Thread.start { // Prod
    while (true) {
        produce.acquire();
        buffer = produce();
        consume.release();
    }
}
Thread.start { // Cons
    while (true) {
        consume.acquire();
        consume(buffer);
        produce.release();
    }
}
```

#### General Semaphores

The following solutions including this one are concerned with buffers of size n:

![alt text](/images/producerConsumerBuffer.png)

```java
Integer[] buffer = new Integer[N];
Semaphore produce = new Semaphore(N);
Semaphore consume = new Semaphore(0);
int start = 0;
int end = 0;
Thread.start { // Prod
    while (true) {
        produce.acquire();
        Integer item = produce();
        buffer[start] = item;
        start = (start + 1) % N;
        // Problem 2 - there is a race condition on start - Problem 1 is the overwriting.
        consume.release();
    }
}
Thread.start { // Cons
    while (true) {
        consume.acquire();
        Integer item = buffer[end];
        end = (end + 1) % N;
        consume(item);
        produce.release();
    }
}
```

Here, semaphores count the number of empty slots in the buffer. We initialize the buffer with N empty slots and 0 full slots.

The thing is this only supports 1 producer and 1 consumer.

Why can't we simply add multiple instances of the producer and consumer?

We create the behavior of having more than 1 producer and consumer by simply looping the threads.

This code isn't applicable to multiple p and c because there are race conditions on adding to the buffer and this could lead to overwriting things. For example, if ther are two producers and they both get to the buffer.start = item line then they both write to the same start index. This means the 2nd producer writes over the first.

#### Multiple Producers And Consumers

We can solve the issue from the previous solution by adding mutexes for the producer and consumer for writing and eating:

```java
final int N = 10;
buffer = new int[N];
permToProduce = new Semaphore(N);
permToConsume = new Semaphore(0);
mutexP = new Semaphore(1);
mutexC = new Semaphore(1);
start = 0;
end = 0;
// Consumers
5.times {
    int id = it;
    Thread.start { // Consumer(id)
        while (true) {
            permToConsume.acquire();
            mutexC.acquire();
            int item = buffer[end];
            println(id + " consumed product " + buffer[end] + " at " + end);
            end = (end + 1) % N;
            mutexC.release();
            permToProduce.release();
            // consumeItem(item);
        }
    }
}
// Producers
5.times {
    int id = it;
    Thread.start { // Producer(id)
        Random r = new Random();
        while (true) {
            int item = r.nextInt(10000); // produceItem();
            permToProduce.acquire();
            mutexP.acquire();
            buffer[start] = item;
            println(id + " added product " + buffer[start] + " at " + start);
            start = (start + 1) % N;
            mutexP.release();
            permToConsume.release();
        }
    }
}
```

## Problem 3 - Readers/Writers

**Resources:** CS 511 Slides

**Problem Description:**

There are shared resources between two types of threads:

- Readers need to access the resource without modifying it
- Writers need to access the resource and may modify it

The problem arises because mutual exclusion is too restrictive. Multiple readers need to access simultaneously and at most 1 writer can access.

How can readers and writers do their job on the buffer without deadlock and starvation?

#### Solution 1 - Priority to Readers

There is only 1 semaphore. In order to write, the writer must take the semaphore and use it. When it is done the 1st reader must grab that same semaphore and then the last reader returns it.

```java
Semaphore resource = new Semaphore(1);
Semaphore numReadersMutex = new Semaphore(1);
int numReaders = 0;
Thread.start { // Writer
    resource.acquire();
    write();
    resource.release();
}
Thread.start { // Reader
    numReadersMutex.acquire();
    numReaders++;
    if (numReaders == 1)
        resource.acquire();
    numReadersMutex.release();
    read();
    numReadersMutex.acquire();
    numReaders--;
    if (numReaders == 0)
        resource.release();
    numReadersMutex.release();
}
```

The problem with this solution is starvation. But, if I assume a fair scheduler won't both readers and writers always get scheduled and its chill? The problem here isn't the scheduler. The problem is that if readers take the resource and a writer comes along, the writer would be blocked. And more readers come along as well. But the readers have to finish reading, so the count of readers will keep flucuating and could never reach 0.

#### Solution 2 - Priority to Writers

We add our mutex's to writers as well.

```java
Semaphore resource = new Semaphore(1);
Semaphore numReadersMutex = new Semaphore(1);
Semaphore numWritersMutex = new Semaphore(1);
Semaphore readTry = new Semaphore(1);
int numReaders = 0;
Thread.start { // Writer
    numWritersMutex.acquire();
    numWriters++;
    if (numWriters == 1)
        readTry.acquire();
    numWritersMutex.release();
    resource.acquire();
    write();
    resource.release();
    numWritersMutex.acquire();
    numWriters--;
    if (numWriters == 0)
        readTry.release();
    numWritersMutex.release();
}
Thread.start { // Reader
    readTry.acquire();
    numReadersMutex.acquire();
    numReaders++;
    if (numReaders == 1)
        resource.acquire();
    numReadersMutex.release();
    readTry.release();
    read();
    numReadersMutex.acquire();
    numReaders--;
    if (numReaders == 0)
        resource.release();
    numReadersMutex.release();
}
```

The issue here is that readers may now starve.

#### Solution 3 - Starvation Free

I feel like the code here seemed a bit more inuintitive than solution 4. You mainly focus on resource and the queue and the queue holds the blocked threads within it and allows the fifo ordering to process the most recent object.

...

#### Solution 4 - Starvation Free 2

No need to review, just another version of a good solution it's a matter of pref to use sol3 or sol4.
