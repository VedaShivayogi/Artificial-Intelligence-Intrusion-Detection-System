from flask import Flask, render_template, request
import os
import numpy as np
from tensorflow.keras.models import load_model
import datetime

from log_analyzer import analyze_log
from csv_analyzer import analyze_csv
from pcap_analyzer import analyze_pcap

app = Flask(__name__)
model = load_model("deep_model.h5")


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        file = request.files.get('file')
        if not file or file.filename == "":
            return "❌ No file selected"

        os.makedirs("uploads", exist_ok=True)
        path = os.path.join("uploads", file.filename)
        file.save(path)

        error = 0
        warning = 0
        packets = 0
        filename = file.filename.lower()
        file_type = "Unknown"

        if filename.endswith((".txt", ".log")):
            error, warning = analyze_log(path)
            file_type = "Log / Text File"
        elif filename.endswith(".csv"):
            error, warning = analyze_csv(path)
            file_type = "CSV Dataset"
        elif filename.endswith(".pcap"):
            packets = analyze_pcap(path)
            file_type = "PCAP Capture"
        else:
            return "❌ Unsupported file format"

        def safe_float(x):
            try: return float(x)
            except: return 0.0

        error = safe_float(error)
        warning = safe_float(warning)
        packets = safe_float(packets)

        X = np.array([error, warning, packets], dtype=np.float32).reshape(1, 3)

        if X.dtype != np.float32:
            return "❌ Data conversion error"

        pred = model.predict(X)
        label = int(np.argmax(pred))
        confidence = round(float(np.max(pred)) * 100, 1)

        prob_normal = round(float(pred[0][0]) * 100, 1)
        prob_probe  = round(float(pred[0][1]) * 100, 1) if pred.shape[1] > 1 else 0.0
        prob_dos    = round(float(pred[0][2]) * 100, 1) if pred.shape[1] > 2 else 0.0

        if label == 0:
            result = "✅ Normal Traffic"
            severity = "low"
            recommendation = "No action required. Continue routine monitoring."
        elif label == 1:
            result = "⚠️ Probe Attack Detected"
            severity = "medium"
            recommendation = "Investigate source IPs. Enable enhanced logging. Review firewall rules."
        else:
            result = "🚨 DoS Attack Detected"
            severity = "high"
            recommendation = "Isolate affected systems immediately. Block suspicious IPs. Alert security team."

        threat_score = error * 2 + warning + (packets / 100)
        risk_level = "Critical" if threat_score > 100 else "High" if threat_score > 50 else "Medium" if threat_score > 10 else "Low"

        file_size = os.path.getsize(path)
        file_size_str = f"{file_size / 1024:.1f} KB" if file_size < 1024*1024 else f"{file_size / (1024*1024):.2f} MB"
        analyzed_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        total_events = int(error + warning)

        return render_template(
            "index.html",
            result=result,
            severity=severity,
            recommendation=recommendation,
            error=int(error),
            warning=int(warning),
            packets=int(packets),
            threat=round(threat_score, 2),
            risk_level=risk_level,
            confidence=confidence,
            prob_normal=prob_normal,
            prob_probe=prob_probe,
            prob_dos=prob_dos,
            file_name=file.filename,
            file_type=file_type,
            file_size=file_size_str,
            analyzed_at=analyzed_at,
            total_events=total_events,
        )

    except Exception as e:
        return f"❌ ERROR: {str(e)}"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
