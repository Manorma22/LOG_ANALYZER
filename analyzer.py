import pandas as pd

def analyze_kpis(data, rsrp_thresh=-100, sinr_thresh=18, cqi_thresh=6):
    df = pd.DataFrame(data)
    df['RSRP_Status'] = df['RSRP'].apply(lambda x: 'PASS' if x >= rsrp_thresh else 'FAIL')
    df['SINR_Status'] = df['SINR'].apply(lambda x: 'OK' if x >= sinr_thresh else 'LOW')
    df['CQI_Status'] = df['CQI'].apply(lambda x: 'GOOD' if x >= cqi_thresh else 'POOR')
    return df
