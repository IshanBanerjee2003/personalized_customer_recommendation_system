import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import yaml

# Load configuration file
with open('config/config.yaml') as file:
    config = yaml.safe_load(file)

# Load the dataset
data = pd.read_csv(config['dataset']['path'])

# Create interaction matrix
interaction_matrix = data.pivot(index='user_id', columns='product_id', values='interaction').fillna(0)

# Split data into training and testing sets
X_train, X_test = train_test_split(interaction_matrix.values, test_size=0.2, random_state=42)

# Define a collaborative filtering model
def create_model(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=(input_dim,)),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(input_dim, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Create and train the model
model = create_model(X_train.shape[1])
model.fit(X_train, X_train, batch_size=config['model']['batch_size'], epochs=config['model']['epochs'])

# Save the trained model
model.save('models/recommendation_model.h5')
print("Model training completed and saved!")
