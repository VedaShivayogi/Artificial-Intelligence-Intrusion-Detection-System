import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Sample training dataset
data = {
    'error': [0, 2, 10, 1, 8, 0, 7],
    'warning': [1, 5, 2, 0, 7, 1, 6],
    'label': [0, 1, 2, 0, 2, 0, 2]  # 0=Normal, 1=Suspicious, 2=Attack
}

df = pd.DataFrame(data)

X = df[['error', 'warning']]
y = df['label']

model = RandomForestClassifier()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model trained and saved!")