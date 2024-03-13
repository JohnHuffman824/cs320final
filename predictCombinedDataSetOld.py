import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Loading the Combined Team Data Set
df = pd.read_csv('combined_team_data.csv') 

# List of Features
# Now the model takes total 6 features for each tiem, instead of 2
X = df[[
    'Home Team Total Yards', 'Away Team Total Yards', 
    'Home Team Passing Yards', 'Away Team Passing Yards',
    'Home Team Passing TD', 'Away Team Passing TD',
    'Home Team Rushing Yards', 'Away Team Rushing Yards',
    'Home Team Rushing TD', 'Away Team Rushing TD',
    'Home Team Turnovers Lost', 'Away Team Turnovers Lost'
]]

# 1 if Home Team Win, else 0
y = df['Winner'].apply(lambda x: 1 if x == 'Home' else 0)  # Ensure y is correctly encoded

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaling the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model Define
model = Sequential([
    Dense(12, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    Dense(64, activation='relu'),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
# Loss is 'binary_crossentropy' because we are doing binary classification
model.compile(optimizer='adam',
              loss='binary_crossentropy', 
              metrics=['accuracy'])

# Train the model
history = model.fit(X_train_scaled, y_train, validation_split=0.2, epochs=50, batch_size=32, verbose=1)

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test_scaled, y_test, verbose=2)
print(f'Test accuracy: {test_acc}')
