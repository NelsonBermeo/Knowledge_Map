## Computer Architecture

To understand how we design out large scaled fleshed out distrubuted systems we first must understand how a computer is designed, at least a high level.

First let's understand the difference between:

B - 1 byte
KB - 1000 bytes - small text files, emails, ...
MB - 1000 KB (1,000,000 - 1 million bytes) - Photos, MP3 songs, PDFs, ...
GB - 1000 MB (1,000,000,000 - 1 billion bytes) - Movies, Games, RAM, ...
TB - 1000 GB (1,000,000,000,000 - 1 trillion bytes) - Large databases, collections of thousands of videos and photos
PB - 1000 TB (1,000,000,000,000,000 - 1 quadrillion bytes) - Massive company databases, data collected by Google, etc. (I didn't think a dataset could be in PB, but apparently CERN's Large Hadron Collider recording almost 300 PB of data from particle collisions)

#### Components

**Disk**

- Also known as "storage" or "SSD" (Solid-state drive)
- Stores all of our data, and does so _persistently_ -> meaning the data will be persisted regardless of the state of the machine (turned on or off) --- This is the upside to using disk instead of RAM or Cache for storing, the other two are not persistent.
- Most modern computers store information in disk on the order of TBs (1 trillion bytes)
- Writing happens in a thousandth of a second

**RAM**

- Random Access Memory
- Used for storing information
- Usually 2-32 GB
- Writing happens almost instantly in micro seconds (a millionth of a second), must faster storing in RAM than Disk

How do we even read from our RAM and Disk? How do we even write data to these components? How do they even talk to each other?

**CPU**

- The brain of our computer, it reads/writes from the RAM and disk(s)
- For instance, writing to RAM occurs when we write code and run it after our code is translated into binary. The CPU can read and execute these instructions which may involve manipulating data stored elsewhere in RAM or on disk.
- An example of reading from disk would be opening a file in your file system and reading it line-by-line.
- All computations are done within the CPU such as addition/substraction/etc --> It fetches instructions from the RAM, decodes those instructions and executes them.
- These fetches are on the terms of milliseconds (thousanth of a second)

**Cache**

- The CPU consists of a cache and is extremely fast memory that lies on the same die as the CPU
- Most CPUs have an L1,L2, and L3 cache which are phyiscal components that are much faster than RAM but can only store data on the order of KB and MB.
- These fetches are on terms of nanoseconds (1 1 billionth of second)
- Cache is mainly used a substitue for RAM
- Whenever a read operation is requested, the cache is checked before RAM and disk -> it is up to the OS to decide what gets stored in the cache because it knows what we access the most
- Applications: web browsers use cache to keep track of frequently accessed web page data to load them faster, ...

Below we have a diagram of how these components work with eachother:

![alt text](/images/computerComponents.png)

**Moore's Law** -> an observation which suggests that the number of transistors in CPU double every two years which is like a proxy for speed. However in recent years this number has sort of plateued.
