Here we will define several mathematical notations for understanding cybersecurity.

First we will start with english meaning.

### Basic Definitions

**3 Basic Properties of security:**

Confidentiality - can untrusted people read my resources
Integrity - can untrusted people write to my resources
Availability - can I use/access my resources

Together these properties are called the CIA Triad.

When we consider information systems in particular, we are also interested in 2 additional dimensions the Information States and the Security Measures in the McCumber Cube:

![alt text](/images/mccumberCube.png)

Information States:

- Transmission
- Storage
- Processing

Security Measures:

- Technology
- Policy and Practice
- Education, Training, and Awareness

**Policies vs. Mechanisms**

Security Policies are statements of what is and not allowed.

Security mechanisms are the means by which policies are enforced.

Considering a system in terms of the set of states the system could be in, for policy -> they define the subsets of secure and insecure states. The mechanisms in this case are the edges (state transitions)

Goals of mechanisms:

- Prevent policy violations
- Detect policy violations
- Recovery: stops violations, then assesses and repairs damage. Prevents service distruption despite volations.

**Assurance** - how much trust can we put in a system? There are 3 steps to providing assurance:

- Specification: state desired and undesired behavior
- Design: translate specs to implementable system components
- Implementation: create system that satsifies design
