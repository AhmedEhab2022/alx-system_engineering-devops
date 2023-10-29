# Explanation of Infrastructure:

**1. Why Additional Servers?**

- Adding multiple servers provides redundancy and high availability. If one server fails, the other can still handle incoming traffic, ensuring continuous service.

**2. Load Balancer (HAproxy):**

- The load balancer distributes incoming traffic evenly across the two web servers using the Round Robin distribution algorithm. This ensures that each server receives an equal share of requests, preventing overload on any single server.

**3. Active-Active vs. Active-Passive Setup:**

- This setup employs an Active-Active configuration, where both web servers are actively serving requests. Active-Active means that both servers are processing traffic simultaneously, enhancing performance and availability. In contrast, an Active-Passive setup would involve one server actively serving while the other remains on standby, only becoming active if the primary server fails.

**4. Database Primary-Replica Cluster:**

- The database operates as a Primary-Replica (Master-Slave) cluster. The Primary node handles write operations and replicates data to the Replica node(s). If the Primary node fails, one of the Replica nodes can be promoted to Primary to ensure continuous data availability.

**5. Difference Between Primary and Replica Nodes:**

- In terms of the application, the Primary node is responsible for handling write operations, such as inserting new data or updating existing records. The Replica node(s) are read-only and mirror the data from the Primary node.

# Issues with this Infrastructure:

**1. Single Points of Failure (SPOF):**

- The web servers and the database cluster each have a single point of failure. If one of the web servers fails or the database Primary node goes down, there will be service disruption until the issue is resolved.

**2. Security Issues:**

- The infrastructure lacks essential security measures such as a firewall and HTTPS encryption. Without a firewall, the servers are vulnerable to unauthorized access, and without HTTPS, data transmitted between the users and the servers is not encrypted.

**3. Lack of Monitoring:**

- There is no monitoring system in place to track server performance, resource usage, or potential security threats.
