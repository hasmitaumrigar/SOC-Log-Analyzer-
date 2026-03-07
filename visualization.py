import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_dashboard(alerts_df, df, save_path="output/dashboard.png"):
    fig, axes = plt.subplots(3,1, figsize=(10,12))

    # 1️⃣ Top Attacking IPs
    top_ips = alerts_df['IP'].value_counts().head(5)
    top_ips.plot(kind='bar', color='tomato', ax=axes[0])
    axes[0].set_title('Top Attacking IPs')
    axes[0].set_xlabel('IP Address')
    axes[0].set_ylabel('Number of Alerts')

    # 2️⃣ Failed Login Attempts
    failed = df[df['Status'] == 401]
    failed_count = failed.groupby(failed['Timestamp'].dt.floor('min')).size()
    failed_count.plot(kind='line', marker='o', color='orange', ax=axes[1])
    axes[1].set_title('Failed Login Attempts Over Time')
    axes[1].set_xlabel('Time')
    axes[1].set_ylabel('Failed Logins')

    # 3️⃣ 404/500 Error Spikes
    error_logs = df[df['Status'].isin([404,500])]
    error_count = error_logs['IP'].value_counts()
    error_count.plot(kind='bar', color='purple', ax=axes[2])
    axes[2].set_title('404/500 Error Spikes per IP')
    axes[2].set_xlabel('IP Address')
    axes[2].set_ylabel('Number of Errors')

    plt.tight_layout()

    # Save the dashboard image
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path)
    print(f"\nDashboard saved as {save_path}")

    plt.show()