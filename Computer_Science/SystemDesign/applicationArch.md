## Application Architecture High Overview

We will dive deeper into the different concepts presented here, but our main goal in this file is to take a step back and understand the system as a whole with moving parts.

The **developer's perspective:**

We write code which will run on a server (we can define a server as a computer that handles requests). Our server would need to store some data (persistantly) and that this data would be stored on a different device than the server.

The **user's perspective:**

A user wanting to use our application would need to communicate with the server and our server would send a response back with the JS, HTML, CSS, or something else. What if there are so users that want to interact with our server? We would need to scale our server!

**Scaling our Server:**

We could add more RAM or upgrade the CPU with more cores and higher clocking speed. However, every computer has a ceiling in terms of upgrades. Upgrading components within the same computer is refferred to as **vertical scaling**.

Instead, we could use **horizontal scaling**, which is making copies of our servers and using multiple. We can distribute user requests among these servers. With horizontal scaling we need to ensure the servers are communicating with eachother and that user requests are being distributed evenly.

To determine which requests go to witch server we use a **load balancer**.

Our servers don't need to work within isolation. For instance website servers could connect to other APIs like Stripe.
