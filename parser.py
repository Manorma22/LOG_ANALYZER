def parse_log(filepath):
    data = []
    with open(filepath, 'r') as file:
        for line in file:
            try:
                ts, rsrp, sinr, cqi = [x.strip() for x in line.strip().split(',')]
                data.append({
                    "Timestamp": ts,
                    "RSRP": float(rsrp),
                    "SINR": float(sinr),
                    "CQI": int(cqi)
                })
            except:
                continue
    return data
