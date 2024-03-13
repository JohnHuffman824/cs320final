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
    'Home Team Turnovers Lost', 'Away Team Turnovers Lost',
    'Home Team Passing Attempts', 'Away Team Passing Attempts',
    'Home Team Passing Completion Percentage', 'Away Team Passing Completion Percentage',
    'Home Team Times Sacked', 'Away Team Times Sacked',
    'Home Team Rushing Attempts', 'Away Team Rushing Attempts',
    'Home Team Rushing Yards per Attempt', 'Away Team Rushing Yards per Attempt',
    'Home Team Penalties', 'Away Team Penalties',
    'Home Team Field Goals Attempted', 'Away Team Field Goals Attempted',
    'Home Team Field Goals Made', 'Away Team Field Goals Made',
    'Home Team 3rd Down Attempts', 'Away Team 3rd Down Attempts',
    'Home Team 3rd Down %', 'Away Team 3rd Down %',
    'Home Team 4th Down Attempts', 'Away Team 4th Down Attempts',
    'Home Team 4th Down Conversion %', 'Away Team 4th Down Conversion %',
    'Home Team 1st Downs', 'Away Team 1st Downs'
]]

# 1 if Home Team Win, else 0
y = df['Winner'] 

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# Define our model architecture
model = Sequential([
    Dense(20, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(80, activation='relu'),
    Dense(160, activation='relu'),
    Dense(80, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
# Loss is 'binary_crossentropy' because we are doing binary classification
model.compile(optimizer='adam',
              loss='binary_crossentropy', 
              metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, validation_split=0.1, epochs=250, batch_size=32, verbose=1)

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
print(f'Test accuracy: {test_acc}')

