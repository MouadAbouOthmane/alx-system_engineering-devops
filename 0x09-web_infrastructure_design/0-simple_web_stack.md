## specifics about Web infrastructure
#### Server:
    A computer that provides services or resources to other computers over a network.
#### Domain Name:
    A human-readable address used to locate resources on the internet, like "www.foobar.com."
#### DNS Record for www.foobar.com:
    Typically a "CNAME" record, mapping "www" to the main domain.
#### Web Server:
    Software/hardware that serves web content to user browsers.
#### Application Server:
    Hosts web applications, handling dynamic aspects.
#### Database:
    Stores and manages data for web applications.
#### Communication with User's Computer:
    Uses HTTP to send web content from the server to the user's browser over the internet.
## explanation of the issues with the described infrastructure:

#### SPOF (Single Point of Failure):
        A Single Point of Failure (SPOF) occurs when there's a critical component or element within the infrastructure that,
        if it fails, can disrupt the entire system. In the described infrastructure, potential SPOFs could be the central 
        web server or database server. If either of these servers fails, it could result in a complete loss of service.
        To mitigate this, redundancy and failover mechanisms can be implemented to ensure service continuity.
        
#### Downtime During Maintenance:
        When maintenance or updates are required, such as deploying new code or restarting the web server, it can lead to downtime. During this downtime, the website or web application may be temporarily inaccessible to users. To minimize this issue, load balancers and redundancy can be used to allow updates and maintenance on one server while another continues to serve users. Additionally, rolling deployments and blue-green deployment strategies can reduce downtime during code updates.
        
#### Limited Scalability:
        If the infrastructure cannot handle high levels of incoming traffic, it means it lacks scalability. To address this issue, the infrastructure should be designed to scale horizontally, which involves adding more servers or resources to handle increased traffic. Load balancing and auto-scaling configurations can help distribute the load and automatically add resources when traffic spikes occur, ensuring the system can handle varying levels of demand without performance degradation.
        
