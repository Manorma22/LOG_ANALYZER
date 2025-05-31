import matplotlib.pyplot as plt

def plot_kpis(df):
    plt.figure(figsize=(10, 4))
    plt.plot(df['Timestamp'], df['RSRP'], marker='o', label='RSRP')
    plt.plot(df['Timestamp'], df['SINR'], marker='s', label='SINR')
    plt.plot(df['Timestamp'], df['CQI'], marker='^', label='CQI')
    plt.xticks(rotation=45)
    plt.xlabel("Timestamp")
    plt.ylabel("KPI Value")
    plt.title("Modem KPI Trends")
    plt.legend()
    plt.tight_layout()
    plt.show()
