# AI-IDS: Artificial Intelligence Intrusion Detection System

An intelligent web-based Intrusion Detection System (IDS) that uses deep learning to analyze network traffic and detect cyber attacks in real-time.

##  Features

- **Multi-format Analysis**: Supports PCAP captures, CSV datasets, and log files
- **Deep Learning Classification**: Neural network trained to detect Normal traffic, Probe attacks, and DoS attacks
- **Real-time Web Interface**: User-friendly Flask-based web application
- **Comprehensive Reporting**: Detailed analysis with confidence scores, threat levels, and security recommendations
- **File Upload System**: Secure file handling with automatic cleanup

##  Prerequisites

- Python 3.8+
- Flask
- TensorFlow/Keras
- NumPy
- Pandas
- Scapy (for PCAP analysis)

## 🛠️ Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/VedaShivayogi/Artificial-Intelligence-Intrusion-Detection-System
cd Artificial-Intelligence-Intrusion-Detection-System
```

### Step 2: Install Dependencies

```bash
pip install flask tensorflow numpy pandas scapy
```

### Step 3: Prepare the Model

The pre-trained deep learning model (`deep_model.h5`) is already included. If you want to retrain:

```bash
python deep_model.py
```

### Step 4: Run the Application

```bash
python app.py
```

### Step 5: Access the Web Interface

Open your browser and navigate to: `http://localhost:5000`

## 🚀 Deployment on Render.com

To deploy this application on Render.com for a live demo:

1. Create a free account on [Render.com](https://render.com)
2. Connect your GitHub repository: https://github.com/VedaShivayogi/Artificial-Intelligence-Intrusion-Detection-System
3. Create a new Web Service
4. Set the runtime to Python 3
5. Set the build command to pip install -r requirements.txt
6. Set the start command to python app.py
7. Deploy the service

Your live demo will be available at the generated Render URL.

## 📖 Usage Guide

### Step-by-Step Analysis Process:

1. **Upload File**: Click "Choose File" and select your network capture file
   - Supported formats: `.pcap`, `.csv`, `.txt`, `.log`

2. **File Processing**: The system automatically detects file type and applies appropriate analysis:
   - **PCAP Files**: Analyzes packet count and traffic patterns
   - **CSV Files**: Processes structured network data
   - **Log Files**: Extracts error and warning counts

3. **AI Analysis**: The deep neural network processes the extracted features:
   - Input features: Error count, Warning count, Packet count
   - Classification: Normal (0), Probe Attack (1), DoS Attack (2)

4. **Results Display**: View comprehensive analysis including:
   - Attack classification with confidence percentage
   - Threat score and risk level
   - Security recommendations
   - Detailed metrics breakdown

### Example Analysis Flow:

```
File Upload → Feature Extraction → Neural Network → Classification → Report Generation
     ↓              ↓                    ↓              ↓              ↓
  .pcap/.csv/.log → [error, warning, packets] → Deep Model → Normal/Attack → Recommendations
```

## 🧠 Model Architecture

The IDS uses a simple yet effective neural network:

```
Input Layer (3 neurons) → Hidden Layer 1 (32 neurons, ReLU)
                        → Hidden Layer 2 (16 neurons, ReLU)
                        → Output Layer (3 neurons, Softmax)
```

**Training Data Features:**

- Error count from logs
- Warning count from logs
- Packet count from captures

**Output Classes:**

- 0: Normal Traffic
- 1: Probe Attack
- 2: DoS Attack

## 📁 Project Structure

```
ai-ids/
├── app.py                 # Main Flask application
├── deep_model.py          # Neural network model creation
├── train_model.py         # Alternative model training (pickle-based)
├── csv_analyzer.py        # CSV file analysis module
├── log_analyzer.py        # Log file analysis module
├── pcap_analyzer.py       # PCAP file analysis module
├── model.py              # Additional model utilities
├── deep_model.h5         # Pre-trained TensorFlow model
├── model.pkl             # Alternative trained model
├── templates/
│   └── index.html        # Web interface template
├── static/
│   └── style.css         # CSS styling
├── uploads/              # Uploaded files directory
├── sample file/          # Sample test files
│   ├── dos_attack.pcap
│   ├── normal_traffic.pcap
│   └── probe_attack.csv
└── output/               # Analysis output directory
```

## 🔍 Analysis Modules

### Log Analyzer (`log_analyzer.py`)

- Parses text/log files for error and warning patterns
- Returns error count and warning count

### CSV Analyzer (`csv_analyzer.py`)

- Processes structured CSV network data
- Extracts relevant security metrics

### PCAP Analyzer (`pcap_analyzer.py`)

- Analyzes packet capture files using Scapy
- Counts total packets and identifies suspicious patterns

## 🎯 Detection Capabilities

| Attack Type    | Detection Method            | Confidence Threshold |
| -------------- | --------------------------- | -------------------- |
| Normal Traffic | Baseline analysis           | >70%                 |
| Probe Attack   | Unusual connection patterns | >60%                 |
| DoS Attack     | High packet volume + errors | >80%                 |

## 📊 Sample Results

### Normal Traffic Analysis:

```
✅ Normal Traffic
Confidence: 92.3%
Threat Score: 5.2 (Low Risk)
Recommendation: No action required. Continue routine monitoring.
```

### DoS Attack Detection:

```
🚨 DoS Attack Detected
Confidence: 87.1%
Threat Score: 156.8 (Critical Risk)
Recommendation: Isolate affected systems immediately. Block suspicious IPs.
```

## 🔗 Demo

[Live Demo](https://ai-ids.onrender.com) - Try the AI-IDS in your browser

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.




