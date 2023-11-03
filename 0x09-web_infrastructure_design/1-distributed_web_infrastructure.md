## Infrastructure Specifics

### For every additional element, why you are adding it
- Additional elements, such as servers, are added to the infrastructure to improve performance, redundancy, and scalability. For example, adding more web servers can distribute the incoming traffic and enhance load handling capacity.

### What are firewalls for
- Firewalls are security devices used to control and filter network traffic. They are designed to protect the infrastructure by allowing or denying incoming and outgoing traffic based on predefined security rules. Firewalls help secure the network from unauthorized access and malicious activity.

### Why is the traffic served over HTTPS
- Traffic is served over HTTPS to ensure secure communication between the client (user's browser) and the server. HTTPS encrypts the data exchanged, protecting it from eavesdropping and tampering. It also verifies the authenticity of the website, which helps prevent man-in-the-middle attacks.

### What monitoring is used for
- Monitoring is used to track the performance, availability, and health of the infrastructure. It helps in identifying issues, potential bottlenecks, and anomalies. Monitoring is crucial for proactive problem resolution, optimizing resource usage, and ensuring the infrastructure meets performance and reliability requirements.

### How the monitoring tool is collecting data
- The monitoring tool collects data by periodically querying various metrics and logs from different components of the infrastructure, such as servers, databases, and network devices. This data can include CPU usage, memory usage, disk space, request response times, error logs, and more. The monitoring tool can use agents installed on servers or utilize APIs and protocols to gather this information.

### Explain what to do if you want to monitor your web server QPS (Queries Per Second)
- To monitor the web server's Queries Per Second (QPS), you can:
  1. Configure your monitoring tool to collect web server access logs and parse them to count the number of queries made to the server per second.
  2. Utilize server performance monitoring tools that can track the number of requests and responses handled by the web server.
  3. Set up custom scripts or use built-in monitoring features to count and record the QPS, then visualize this data for analysis. 

## Issues with the Infrastructure

### Why terminating SSL at the load balancer level is an issue
- Terminating SSL at the load balancer level can be an issue because it places an extra load on the load balancer, potentially limiting its capacity to handle other tasks. It may also expose the decrypted traffic to potential security risks, which would not occur if SSL termination happened at the web servers. To resolve this, SSL termination should be distributed across web servers or offloaded to a dedicated SSL termination server.

### Why having only one MySQL server capable of accepting writes is an issue
- Having only one MySQL server capable of accepting writes is a single point of failure (SPOF). If that server goes down, it can lead to data loss and downtime. To address this, a master-slave or multi-master MySQL setup should be implemented. This ensures data redundancy and high availability, as multiple servers can accept writes, and data is automatically replicated between them.

### Why having servers with all the same components (database, web server, and application server) might be a problem
- Having servers with identical components can be problematic because it lacks diversity and can lead to common points of failure. If a specific component or software version has a vulnerability or issue, it affects all servers in the same way. Introducing diversity in the infrastructure, such as using different server types or versions, can help in reducing the impact of potential issues and improving resilience.

