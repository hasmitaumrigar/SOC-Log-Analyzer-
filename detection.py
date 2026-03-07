import pandas as pd

def detect_bruteforce(df):
    alerts = []
    failed = df[df["Status"] == 401]
    failed_count = failed.groupby("IP").size()
    for ip, count in failed_count.items():
        if count >= 3:
            severity = "Medium"
            if count >= 6:
                severity = "High"
            alerts.append({
                "IP": ip,
                "Attack Type": "Brute Force Attempt",
                "Count": count,
                "Severity": severity
            })
    return alerts

def detect_dos(df):
    alerts = []
    df["Minute"] = df["Timestamp"].dt.floor("min")
    request_count = df.groupby(["IP", "Minute"]).size()
    for (ip, minute), count in request_count.items():
        if count >= 5:
            alerts.append({
                "IP": ip,
                "Attack Type": "Possible DoS",
                "Count": count,
                "Severity": "High"
            })
    return alerts

def detect_error_spike(df):
    alerts = []
    error_logs = df[df["Status"].isin([404, 500])]
    error_count = error_logs.groupby("IP").size()
    for ip, count in error_count.items():
        if count >= 3:
            alerts.append({
                "IP": ip,
                "Attack Type": "Suspicious Error Spike (404/500)",
                "Count": count,
                "Severity": "Medium"
            })
    return alerts