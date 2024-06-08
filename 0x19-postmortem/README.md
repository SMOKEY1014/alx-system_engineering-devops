# Postmortem: Web Stack Outage

## Issue Summary

**Duration:**

- **Outage Start:** March 15, 2024, 08:00 AM GMT
- **Outage End:** March 15, 2024, 10:30 AM GMT

**Impact:**

- The main e-commerce website was completely down. Users were unable to access the site, resulting in 100% of users being affected. This led to a loss of sales and customer frustration.

**Root Cause:**

- The root cause was an exhausted database connection pool due to a misconfiguration in the application server settings, leading to all connections being consumed and no new connections being established.

## Timeline

- **08:00 AM GMT:** Issue detected via monitoring alert indicating high error rates and failed health checks.
- **08:05 AM GMT:** An engineer on call verified the alert and noticed the website was unresponsive.
- **08:10 AM GMT:** Initial investigation focused on the web servers; assumption was a potential DDoS attack.
- **08:30 AM GMT:** Misleading path - Network and firewall logs analyzed, but no signs of unusual traffic were found.
- **08:45 AM GMT:** Escalation to the database team as high query times were noticed.
- **09:00 AM GMT:** Database connections were examined, revealing all connections were in use and not being released.
- **09:15 AM GMT:** Misleading path - Cache server and load balancer configurations were checked, but no issues were identified.
- **09:30 AM GMT:** Application logs reviewed, identifying repeated connection timeouts.
- **09:45 AM GMT:** Configuration issue in the application server's connection pool settings identified.
- **10:00 AM GMT:** Connection pool settings corrected and application servers restarted.
- **10:30 AM GMT:** Website functionality fully restored, and normal operations resumed.

## Root Cause and Resolution

**Root Cause:**  
The application server was configured with a maximum connection pool size that was too low, causing the pool to exhaust quickly under load. As a result, no new connections could be established to the database, leading to the website becoming unresponsive.

**Resolution:**  
The connection pool size configuration in the application server was increased to handle more connections. Additionally, the server was restarted to apply the new settings. Monitoring was set up to alert if the connection pool usage reached critical levels again.

## Corrective and Preventative Measures

**Improvements/Fixes:**

- **Increase Connection Pool Size:** Adjust the maximum number of connections to accommodate peak traffic loads.
- **Monitor Connection Pool Usage:** Implement monitoring to track the connection pool usage and alert if it exceeds a predefined threshold.
- **Optimize Database Queries:** Review and optimize long-running queries to ensure efficient use of connections.
- **Regular Load Testing:** Conduct periodic load testing to ensure the system can handle high traffic volumes without exhausting resources.
- **Review Configuration Management:** Implement a configuration review process to ensure all settings are optimal for performance and scalability.

**Tasks:**

1. **Patch Application Server:** Apply the updated configuration settings across all environments.
2. **Add Monitoring:** Implement detailed monitoring on database connection pool usage.
3. **Optimize Queries:** Audit and optimize database queries to reduce connection hold times.
4. **Conduct Load Testing:** Schedule and perform regular load tests to validate system performance.
5. **Review and Update Documentation:** Update internal documentation to reflect the new configuration settings and monitoring protocols.

By addressing these issues, we aim to prevent similar outages in the future and ensure a more resilient and reliable web stack.
