import pandas as pd
import numpy as np

# Generate synthetic data for user-product interactions
n_users = 10000
n_products = 500

user_ids = np.random.randint(1, n_users + 1, size=50000)
product_ids = np.random.randint(1, n_products + 1, size=50000)
interactions = np.random.randint(0, 2, size=50000)  # 1: interacted, 0: no interaction

df = pd.DataFrame({
    'user_id': user_ids,
    'product_id': product_ids,
    'interaction': interactions
})

df.to_csv('dataset/raw/user_product_interactions_raw.csv', index=False)
print("Synthetic dataset generated!")
