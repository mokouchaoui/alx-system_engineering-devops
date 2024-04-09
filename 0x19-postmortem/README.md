![cat logo](https://raw.githubusercontent.com/mokouchaoui/alx-system_engineering-devops/master/0x19-postmortem/_6395cd10-44f7-4454-9299-ba4a2d7dc7d8.jpeg)

**Issue Summary:**

- **Duration:** 
  - Start Time: November 5, 2023, 10:00 AM (UTC)
  - End Time: November 5, 2023, 1:30 PM (UTC)

- **Impact:** 
  - The outage affected our e-commerce website, resulting in a 3.5-hour downtime.
  - Users experienced slow loading times, incomplete transactions, and some reported errors.
  - Approximately 25% of our users were affected.

**Timeline:**

- **Detection Time:**
  - November 5, 2023, 10:15 AM (UTC)

- **How Issue Was Detected:**
  - Monitoring alert triggered when server response times exceeded predefined thresholds.

- **Actions Taken:**
  - Investigated the web server logs, application logs, and database performance.
  - Assumed initial hypothesis that high traffic was the root cause.

- **Misleading Investigation/Debugging Paths:**
  - Initially suspected a DDoS attack due to increased traffic but ruled it out after analyzing traffic patterns.
  - Investigated potential database performance issues but found no anomalies.

- **Escalation:**
  - The incident was escalated to the DevOps and Database teams for further investigation and resolution.

- **Resolution:**
  - Identified that a critical configuration file for the web server had been accidentally deleted, causing misrouting of traffic.
  - Restored the missing configuration file and restarted the web server.

**Root Cause and Resolution:**

- **Root Cause:**
  - The root cause of the issue was the accidental deletion of a critical web server configuration file.
  - This resulted in misrouting of incoming requests and increased server load, leading to slow response times and errors.

- **Resolution:**
  - The missing configuration file was recovered from backups.
  - The web server was reconfigured with the restored file.
  - After reconfiguration, the web server was restarted to apply the changes.
  - Server response times returned to normal, and the website was fully operational.

**Corrective and Preventative Measures:**

- **Improvements/Fixes:**
  - Enhance monitoring and alerting systems to immediately detect and notify about configuration file changes.
  - Implement stricter access controls and permissions on critical configuration files to prevent accidental deletion.
  - Regularly audit configuration files to identify any deviations from the expected state.
  - Develop and document a rollback procedure in case of critical configuration file loss.

- **Tasks to Address the Issue:**
  - Enhance monitoring: Implement real-time file integrity checks for critical configuration files and set up automated alerts for any changes.
  - Access control review: Review and improve access controls and permissions on critical configuration files to prevent unauthorized modifications.
  - Configuration file backups: Regularly back up critical configuration files and ensure that reliable recovery procedures are in place.
