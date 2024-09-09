import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load raw data
raw_data = pd.read_csv('dataset/raw/user_product_interactions_raw.csv')

# Normalize interaction values using MinMaxScaler
scaler = MinMaxScaler()
raw_data['interaction'] = scaler.fit_transform(raw_data[['interaction']])

# Save preprocessed data
raw_data.to_csv('dataset/processed/user_product_interactions_processed.csv', index=False)
print("Data preprocessing completed!")
