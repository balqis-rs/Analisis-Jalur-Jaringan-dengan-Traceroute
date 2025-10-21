import subprocess
import re
import matplotlib.pyplot as plt

def run_traceroute(target):
    print(f"Menjalankan traceroute ke {target}...\n")
    result = subprocess.run(["traceroute", target], capture_output=True, text=True)
    return result.stdout

def parse_traceroute(output):
    hops = []
    for line in output.splitlines():
        match = re.findall(r"(\d+\.\d+\.\d+\.\d+|\*)\s+(\d+\.\d+)\s+ms", line)
        if match:
            ip = match[0][0]
            latency = float(match[0][1]) if match[0][0] != "*" else None
            hops.append((ip, latency))
    return hops

def analyze_hops(hops):
    print("Analisis hasil traceroute:")
    for i, (ip, latency) in enumerate(hops):
        status = "MACET" if latency and latency > 100 else "LANCAR"
        print(f"Hop {i+1}: IP={ip}, Latency={latency} ms → {status}")
    return hops

def plot_latency(hops):
    labels = [f"Hop {i+1}" for i in range(len(hops))]
    latencies = [lat if lat else 0 for _, lat in hops]
    colors = ['red' if lat > 100 else 'green' for lat in latencies]

    plt.figure(figsize=(10, 5))
    plt.bar(labels, latencies, color=colors)
    plt.xlabel("Hop")
    plt.ylabel("Latency (ms)")
    plt.title("Grafik Latency per Hop")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    target_host = "8.8.8.8"  # Ganti dengan IP tujuanmu
    output = run_traceroute(target_host)
    hops = parse_traceroute(output)
    analyzed = analyze_hops(hops)
    plot_latency(analyzed)
