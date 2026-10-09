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
- Stores all of our data, and does so _persistently_ -> meaning the data will be persisted regardless of the state of the machine (turned on or off)
- Most modern computers store information in disk on the order of TBs (1 trillion bytes)
- Writing happens in a thousandth of a second

**RAM**

- Random Access Memory
- Used for storing information
- Usually 2-32 GB
- Writing happens almost instantly in micro seconds (a millionth of a second), must faster storing in RAM than Disk

How do we even read from our RAM and Disk? How do we even write data to these components? How do they even talk to each other?

**CPU**

- The brain of our computer
