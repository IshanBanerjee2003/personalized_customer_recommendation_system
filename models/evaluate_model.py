import tensorflow as tf
import pandas as pd
from sklearn.metrics import mean_squared_error
import yaml

# Load configuration file
with open('config/config.yaml') as file:
    config = yaml.safe_load(file)

# Load the dataset and model
data = pd.read_csv(config['dataset']['path'])
model = tf.keras.models.load_model('models/recommendation_model.h5')

# Prepare test data
interaction_matrix = data.pivot(index='user_id', columns='product_id', values='interaction').fillna(0)
_, X_test = train_test_split(interaction_matrix.values, test_size=0.2, random_state=42)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(X_test, predictions)
print(f"Model Test MSE: {mse:.4f}")
