# Artificial Intelligence Intrusion Detection System

Demo: https://artificial-intelligence-intrusion-darp.onrender.com

## Description
This application analyzes uploaded log, CSV, and PCAP files to detect normal traffic, probe attacks, and DoS attacks.

## Local setup
1. Use Python 3.11.
2. Create a virtual environment in the project folder.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python app.py
   ```

## Notes
- `app.py` now handles TensorFlow missing situations by using a fallback classifier if `deep_model.h5` is not loadable.
- For Render deployment, the project uses `render.yaml` with `pythonVersion: 3.11`.
