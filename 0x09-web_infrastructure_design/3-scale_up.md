
# Application server vs web server

This is a basic network diagram that shows the difference between an application server and a web server, and how they can work together to serve dynamic web content.

## Components

- **Web server**: A web server is a software that handles HTTP requests from clients (such as web browsers) and serves static web content (such as HTML, CSS, images, etc.). In this diagram, I used **Nginx**⁴ as an example of a web server. Nginx can also act as a reverse proxy, load balancer, and HTTP cache.
- **Application server**: An application server is a software that provides application logic and services (such as database access, security, transaction management, etc.) to support dynamic web content (such as scripts, servlets, EJBs, etc.). In this diagram, I used **Tomcat** as an example of an application server. Tomcat is a Java-based web container that can execute Java servlets and JSPs.
- **Database server**: A database server is a software that stores and manages data for applications. In this diagram, I used **MySQL** as an example of a database server. MySQL is a relational database management system that supports SQL queries and transactions.
- **Load balancer**: A load balancer is a software or hardware device that distributes incoming requests across multiple servers to optimize performance, reliability, and scalability. In this diagram, I used **HAProxy** as an example of a load balancer. HAProxy is an open source software that can balance TCP and HTTP traffic and support high availability and clustering.

## Architecture

The network diagram shows how the components are connected and interact with each other. The main steps are:

- A client sends an HTTP request to the web server through the internet.
- The web server receives the request and checks if it can serve the requested resource (such as a static HTML page or an image) from its local cache or file system. If yes, it returns the resource to the client. If not, it forwards the request to the load balancer.
- The load balancer receives the request and selects one of the two application servers based on its load balancing algorithm (such as round robin, least connections, etc.). It then passes the request to the selected application server.
- The application server receives the request and executes the appropriate application logic (such as a script, a servlet, or an EJB) to generate dynamic web content. It may also communicate with the database server to retrieve or update data. It then returns the dynamic web content to the load balancer.
- The load balancer receives the dynamic web content from the application server and forwards it to the web server.
- The web server receives the dynamic web content from the load balancer and sends it back to the client.

## Advantages

The advantages of using this architecture are:

- It separates the concerns of serving static and dynamic web content, which improves modularity, maintainability, and security.
- It improves performance by caching static resources on the web server and distributing dynamic requests across multiple application servers.
- It enhances reliability by using HAProxy to detect and avoid failed servers and provide failover mechanisms.
- It increases scalability by allowing adding or removing servers as needed without affecting the overall functionality.

## References

: https://www.nginx.com/
: http://tomcat.apache.org/
: https://www.mysql.com/
: http://www.haproxy.org/
