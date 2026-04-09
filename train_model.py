from flask import Flask, render_template, request
import pickle
from log_analyzer import analyze_log
from pcap_analyzer import analyze_pcap
import os

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['file']
    
    if not file:
        return "No file uploaded"

    filepath = os.path.join("uploads", file.filename)
    file.save(filepath)

    # LOG / TXT
    if file.filename.endswith(".txt") or file.filename.endswith(".log"):
        error, warning = analyze_log(filepath)
        prediction = model.predict([[error, warning]])[0]

        if prediction == 0:
            result = "✅ Normal Activity"
        elif prediction == 1:
            result = "⚠️ Suspicious Activity"
        else:
            result = "❌ Attack Detected"

        return render_template("index.html",
                               result=result,
                               error=error,
                               warning=warning)

    # PCAP
    elif file.filename.endswith(".pcap"):
        packets, result = analyze_pcap(filepath)

        return render_template("index.html",
                               result=result,
                               packets=packets)

    else:
        return "Unsupported file type"

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True)