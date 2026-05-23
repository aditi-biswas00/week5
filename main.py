from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

# Load datasets
sales = pd.read_csv(DATA_DIR / "sales_data.csv")
customers = pd.read_csv(DATA_DIR / "customer_data.csv")

print(sales.head())
print(customers.head())

# Align the customer ID column name before merging
customers = customers.rename(columns={"CustomerID": "Customer_ID"})

# Example merge
merged_data = pd.merge(sales, customers, on='Customer_ID', how='inner')

# Example aggregation
print(merged_data.groupby('Customer_ID').size())
