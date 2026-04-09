from scapy.all import rdpcap

def analyze_pcap(filepath):
    packets = 0

    try:
        data = rdpcap(filepath)
        packets = len(data)

    except Exception as e:
        print("PCAP Analyzer Error:", e)

    # ✅ MUST return integer
    return int(packets)