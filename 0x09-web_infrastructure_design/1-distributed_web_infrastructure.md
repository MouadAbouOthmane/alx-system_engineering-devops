## Infrastructure Specifics

### For every additional element, why you are adding it
- Additional elements, such as servers or resources, are added to enhance performance, redundancy, and scalability. For example, adding more web servers can distribute traffic and improve load handling capacity.

### What distribution algorithm your load balancer is configured with and how it works
- The load balancer is configured with a Round Robin distribution algorithm. It evenly distributes incoming requests to available backend servers in a circular manner. Each server gets its turn to handle requests, ensuring a balanced load across the infrastructure.

### Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
- The load balancer is set up for an Active-Active configuration. In an Active-Active setup, all backend servers are actively serving requests simultaneously. This ensures high availability and optimal resource utilization. In contrast, Active-Passive setup involves one server actively serving requests, while others remain passive until failover is needed.

### How a database Primary-Replica (Master-Slave) cluster works
- In a Primary-Replica (Master-Slave) cluster, there is one primary (master) database server and one or more replica (slave) database servers. The primary server handles write operations and data changes, while replica servers replicate data from the primary server. This setup provides redundancy and load distribution.

### What is the difference between the Primary node and the Replica node in regard to the application
- The Primary node in a database cluster is responsible for handling write operations, making it the authoritative source for data changes. The application primarily interacts with the Primary node when writing data. Replica nodes, on the other hand, serve read-only requests, providing load distribution for read-heavy workloads. Applications can query Replica nodes for read operations, reducing the load on the Primary node and enhancing read performance.

## Issues with the Infrastructure

### Where are SPOF (Single Points of Failure)
- The potential Single Points of Failure in this infrastructure include the load balancer, the primary database server, and any shared components that lack redundancy. If any of these elements fails, it can disrupt the entire system. To mitigate this, redundancy and failover mechanisms should be implemented for these components.

### Security issues (no firewall, no HTTPS)
- The absence of a firewall exposes the infrastructure to security risks, as it lacks protection from unauthorized access and malicious traffic. Not serving traffic over HTTPS leaves data transmission vulnerable to eavesdropping and tampering. Implementing a firewall and enabling HTTPS are essential for security.

### No monitoring
- The absence of monitoring is a significant issue. Monitoring is crucial for tracking performance, identifying problems, and ensuring infrastructure health. Without monitoring, it's challenging to proactively address issues, optimize resource usage, and meet performance and reliability requirements. Monitoring tools should be implemented to address this issue.

