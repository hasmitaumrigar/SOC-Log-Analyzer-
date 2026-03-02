***SOC-Log-Analyzer***

**Overview**

This project is a Security Operations Center (SOC) Log Analyzer built in Python. It parses Apache web server logs, detects security incidents, visualizes trends, and generates a professional PDF report. The project is designed to help SOC analysts monitor potential threats such as brute-force attacks, DoS attempts, and error spikes.

**Fetures**

***1. Log Parsing***

Reads Apache logs using regex.

Extracts fields: IP, Timestamp, Method, URL, Status, Size.

Adds a per-minute timestamp for detecting rapid requests.

***2. Threat Detection***

Brute-force attacks → Flags IPs with ≥3 failed logins (401).

DoS detection → Flags IPs with ≥5 requests per minute.

Error spikes → Flags IPs generating ≥3 HTTP 404/500 errors.
Generates a combined alerts CSV (alerts.csv).

***3. Visualization***

Plots top attacking IPs, failed login attempts over time, and error spikes.

Creates a dashboard image (dashboard.png) summarizing all metrics.

***4. PDF Report***

Automatically generates a 2-page professional report (SOC_Report.pdf).

Page 1: Title, Objective, and Sample Logs (with readable timestamps).

Page 2: Alerts Table (Attack Types truncated) + Dashboard Visualization.

**Technologies Used**

Python 3

pandas → Data processing and manipulation

matplotlib → Charts and visualizations

fpdf → PDF report generation

**Project Structure**

SOC_Log_Analyzer/
analyzer.py          # Main script
detection.py         # Functions to detect brute-force, DoS, error spikes
visualization.py     # Charts and dashboard plotting
report.py            # PDF generation
logs/apache.log      # Sample Apache log file
output/             # CSV, dashboard image, and PDF report outputs

**Learning / Mistake**

During development, I initially added the full datetime as the “Minute” column, which made the PDF table unreadable because the timestamps were too wide. 

I fixed it by formatting the Minute column as HH:MM, making the sample logs table clean and readable in the report.

This taught me the importance of data formatting for reporting and visualization, especially when working with professional documents.

**Conclusion**

This project demonstrates how to process web logs, detect anomalies, visualize attacks, and generate professional SOC reports.
