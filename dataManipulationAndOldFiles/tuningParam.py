import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers.legacy import Adam, SGD, RMSprop

# Loading the Combine Team dataset
df = pd.read_csv('combined_team_data.csv')

# List of Features
# Now the model takes total 6 features for each tiem, instead of 2
X = df[['Home Team Total Yards', 'Away Team Total Yards',
        'Home Team Passing Yards', 'Away Team Passing Yards',
        'Home Team Passing TD', 'Away Team Passing TD',
        'Home Team Rushing Yards', 'Away Team Rushing Yards',
        'Home Team Rushing TD', 'Away Team Rushing TD',
        'Home Team Turnovers Lost', 'Away Team Turnovers Lost']]

# 1 if Home Team Win, else 0
y = df['Winner'].apply(lambda x: 1 if x == 'Home' else 0)

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaling the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Function for creating and compiling the model
# based on our custom model
def create_model(num_nodes, learning_rate, optimizer_choice):
    model = Sequential([
        Dense(num_nodes, activation='relu', input_shape=(X_train_scaled.shape[1],)),
        Dense(num_nodes // 2, activation='relu'),
        Dense(1, activation='sigmoid')
    ])

    # List of optimizations
    optimizers = {
        'adam': Adam(learning_rate=learning_rate),
        'sgd': SGD(learning_rate=learning_rate),
        'rmsprop': RMSprop(learning_rate=learning_rate)
    }
    optimizer = optimizers[optimizer_choice]
    
    model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Function for hyperparameter tuning
# It takes list of number of nodes, learning_rate, and optimizers
def tune_hyperparameters(node_options, learning_rates, optimizers, X_train_scaled, y_train, X_test_scaled, y_test):
    best_acc = 0.5
    best_config = None
    
    for nodes in node_options:
        for lr in learning_rates:
            for opt in optimizers:
                model = create_model(nodes, lr, opt)
                model.fit(X_train_scaled, y_train, epochs=50, batch_size=32, verbose=0)  # Reduce verbosity for tuning
                _, test_acc = model.evaluate(X_test_scaled, y_test, verbose=0)  # Silent evaluation
                
                print(f"Nodes: {nodes}, Learning Rate: {lr}, Optimizer: {opt}, Test Accuracy: {test_acc}")
                
                if test_acc > best_acc:
                    best_acc = test_acc
                    best_config = {'nodes': nodes, 'learning_rate': lr, 'optimizer': opt}
    
    return best_config, best_acc

# Hyperparameters to test
# List of node options, learning rates, optimizers
node_options = [32, 64, 128, 256, 512]
learning_rates = [0.1, 0.01, 0.001, 0.0001]
optimizers = ['adam', 'sgd', 'rmsprop']

# Tuning hyperparameters
best_config, best_acc = tune_hyperparameters(node_options, learning_rates, optimizers, X_train_scaled, y_train, X_test_scaled, y_test)
print(f'Best Configuration: Nodes - {best_config["nodes"]}, Learning Rate - {best_config["learning_rate"]}, Optimizer - {best_config["optimizer"]}, Test Accuracy: {best_acc}')