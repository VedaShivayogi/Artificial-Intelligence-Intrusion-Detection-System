import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Dataset (extended)
data = {
    'error':    [0,2,10,1,8,0,7,15,3,12],
    'warning':  [1,5,2,0,7,1,6,3,8,4],
    'packets':  [100,300,1200,200,900,150,800,2000,400,1500],
    'label':    [0,1,2,0,2,0,2,2,1,2]  
    # 0=Normal, 1=Probe, 2=DoS
}

df = pd.DataFrame(data)

X = df[['error','warning','packets']].values
y = df['label'].values

model = Sequential()
model.add(Dense(32, activation='relu', input_dim=3))
model.add(Dense(16, activation='relu'))
model.add(Dense(3, activation='softmax'))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X, y, epochs=150)

model.save("deep_model.h5")

print("✅ Deep Model Ready")