#### System Defenses

There are a number of features that your operating system has to defend against memory vulnerability exploits:

1. Memory Protection (MMU)
2. Address Space Layout Randomization

Most systems have a **memory management unit (MMU)** that is capable of enforcing read-write-execute permissions on address ranges.

To reduce the likeelihood of shellcode exploits, writable regions should always be non-executable (NX)

There is also **address space layout randomization (ASLR)**.

Essentially, attackers need to determine instruction addresses at runtime for precise control-flow hijacking. But the OS makes this more difficult by randomizing the location of program memory sections at runtime.

#### Compiler Defenses

Some protections can be compiled into the binary itself. **Stack canaries** and **point authentication codes** are 2 ways to prevent hijacking that can be automatically added by the compler itself.

**Stack Canaries** are a known value placed on the stack before the saved frame pointer and the return address that can be validated before actually returning.
