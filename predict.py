import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


df1 = pd.read_csv('restructured_2019_season_data.csv') 
df2 = pd.read_csv('restructured_2020_season_data.csv') 
df3 = pd.read_csv('restructured_2021_season_data.csv') 
df4 = pd.read_csv('restructured_2022_season_data.csv') 


df = pd.concat([df1, df2, df3, df4], axis=0)

# print(df.shape)



X = df[['Home Team Total Yards', 'Away Team Total Yards', 'Home Team Turnovers', 'Away Team Turnovers']]
y = df['Winner']
# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
history = model.fit(X_train_scaled, y_train, validation_split=0.2, epochs=50, batch_size=32, verbose=1)
test_loss, test_acc = model.evaluate(X_test_scaled, y_test, verbose=2)
print(f'Test accuracy: {test_acc}')


new_game = [[221,281,0,3]]  # Example features: Home Yard, Away Yard, Home Turnover, Away Turnover

# Scale the new game data
new_game_scaled = scaler.transform(new_game)

# Predict
prediction = model.predict(new_game_scaled)
predicted_winner = 'Home Team' if prediction >= 0.5 else 'Away Team'
print(f'Predicted Winner: {predicted_winner}, Probability: {prediction[0][0]}')


def predict_and_evaluate(dataset_path, model, scaler):
    # Load the dataset
    df_new = pd.read_csv(dataset_path)
    
    # Select the features and target variable
    X_new = df_new[['Home Team Total Yards', 'Away Team Total Yards', 'Home Team Turnovers', 'Away Team Turnovers']]
    y_new = df_new['Winner']
    
    # Scale the features
    X_new_scaled = scaler.transform(X_new)
    
    # Evaluate the model
    loss, accuracy = model.evaluate(X_new_scaled, y_new, verbose=2)
    
    print(f'Accuracy on new dataset: {accuracy}')
    return accuracy

# Most current season
dataset_path = 'restructured_2023_season_data.csv'  # Update this path as necessary
predict_and_evaluate(dataset_path, model, scaler)