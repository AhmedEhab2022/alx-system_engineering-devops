# Explanation of Infrastructure:

**1. Firewalls:**

- Firewalls are added to control incoming and outgoing network traffic. They act as a security barrier, allowing only authorized traffic to pass through, enhancing the infrastructure's security by protecting against unauthorized access and potential attacks.

**2. SSL Certificate and Serving Traffic Over HTTPS:**

- An SSL certificate is added to encrypt data transmitted between users and the web server. HTTPS ensures secure communication, safeguarding user data from interception and tampering during transmission, providing confidentiality and integrity of the exchanged information.

**3. Monitoring Clients (Datadog):**

- Datadog is used as the monitoring tool to collect data on server performance, resource usage, security incidents, and user interactions. Monitoring is crucial for real-time analysis, issue detection, capacity planning, and ensuring the infrastructure's reliability and stability.

**4. Why Traffic Served Over HTTPS:**

- Traffic is served over HTTPS to encrypt data transmitted between users and the web server. This encryption ensures data confidentiality, preventing unauthorized access and eavesdropping, and guarantees the integrity and authenticity of the information exchanged between users and the website.

**5. Monitoring and Data Collection:**

- Monitoring is used to track server metrics, errors, and user interactions. Datadog collects data by integrating with server logs, metrics, and events. It analyzes this data, providing insights into server performance, user behavior, and security incidents, enabling proactive issue resolution and infrastructure optimization.

**6. Monitoring Web Server QPS (Queries Per Second):**

- To monitor web server QPS, Datadog collects and analyzes server logs and metrics related to incoming queries. By setting up specific log queries and metrics filters, administrators can monitor QPS trends, identify spikes or anomalies, and take proactive measures to optimize server performance and prevent overloads.

# Issues with this Infrastructure:

**1. Terminating SSL at the Load Balancer Level:**

- Terminating SSL at the load balancer level can be an issue because it exposes unencrypted traffic within the internal network. If an attacker gains access to the internal network, they could potentially intercept sensitive data transmitted between the load balancer and the web servers.

**2. Having Only One MySQL Server Capable of Accepting Writes:**

- Having only one MySQL server capable of accepting writes creates a single point of failure. If the primary MySQL server fails, write operations cannot be performed, leading to data inconsistency and application downtime.

**3. Having Servers with All the Same Components (Database, Web Server, and Application Server):**

- Having servers with identical components poses a problem regarding diversity and fault tolerance. If there is a vulnerability or issue with a specific component, it could affect all servers simultaneously.
