import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense

# Load data for the Chiefs and the 49ers
chiefs_data = pd.read_csv('chiefs_2023_data.csv')
fortyniners_data = pd.read_csv('49ers_2023_data.csv')

# Merge data for both teams into one DataFrame
merged_data = pd.concat([chiefs_data, fortyniners_data], ignore_index=True)

# Select relevant features for prediction
selected_features = ['PointsScored', 'TotalYards', 'Turnovers',
                     'OpponentPointsScored', 'OpponentTotalYards', 'OpponentTurnovers']

# Create feature vectors for each game
X = merged_data[selected_features].values

# Create labels indicating the outcome of each game (1 for Chiefs win, 0 for 49ers win)
y = np.where(merged_data['Win/Loss'] == 'W', 1, 0)

# Split the data into training, validation, and testing sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)

# Define the neural network architecture
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train_scaled, y_train, validation_data=(X_val_scaled, y_val), epochs=50, batch_size=32, verbose=1)

# Evaluate the model
loss, accuracy = model.evaluate(X_test_scaled, y_test, verbose=0)
print(f'Test Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}')

# Make predictions for a game between the Chiefs and the 49ers
chiefs_stats = ...  # Extract stats for the Chiefs
fortyniners_stats = ...  # Extract stats for the 49ers
game_features = np.array([chiefs_stats, fortyniners_stats])
game_features_scaled = scaler.transform(game_features)
prediction = model.predict(game_features_scaled)
print(f'Predicted winner: {"Chiefs" if prediction > 0.5 else "49ers"}')
