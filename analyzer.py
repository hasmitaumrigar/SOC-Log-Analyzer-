import re
import pandas as pd
from datetime import datetime
from detection import detect_bruteforce, detect_dos, detect_error_spike
from visualization import plot_dashboard  # import the function

LOG_FILE = "logs/apache.log"

log_pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(GET|POST) (.*?) HTTP/1.1" (\d+) (\d+)'

def parse_apache_log(file_path):
    data = []
    with open(file_path, "r") as file:
        for line in file:
            match = re.search(log_pattern, line)
            if match:
                ip = match.group(1)
                timestamp = datetime.strptime(match.group(2), "%d/%b/%Y:%H:%M:%S")
                method = match.group(3)
                url = match.group(4)
                status = int(match.group(5))
                size = int(match.group(6))
                data.append([ip, timestamp, method, url, status, size])
    df = pd.DataFrame(data, columns=["IP", "Timestamp", "Method", "URL", "Status", "Size"])
    return df

if __name__ == "__main__":
    df = parse_apache_log(LOG_FILE)

    print("\nParsed Logs:\n")
    print(df)

    # Run detection
    brute_alerts = detect_bruteforce(df)
    dos_alerts = detect_dos(df)
    error_alerts = detect_error_spike(df)

    # Combine alerts
    all_alerts = brute_alerts + dos_alerts + error_alerts

    print("\n🚨 ALERTS DETECTED:\n")
    for alert in all_alerts:
        print(alert)

    # Save alerts to CSV
    if all_alerts:
        alerts_df = pd.DataFrame(all_alerts)
        alerts_df.to_csv("output/alerts.csv", index=False)
        print("\nAlerts saved to output/alerts.csv")

        # Plot dashboard
        plot_dashboard(alerts_df, df, save_path="output/dashboard.png")
    from report import generate_report

# Generate PDF report
generate_report(df, alerts_df, dashboard_path="output/dashboard.png", output_pdf="output/SOC_Report.pdf")