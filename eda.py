import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load dataset (merged version)
df = pd.read_csv('data.csv')

# Display information
print("=== FRAUD DETECTION EDA ===")
print(f"Dataset shape: {df.shape}")
print(df.head())

# Statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Visualization
plt.figure(figsize=(12, 8))
df.hist(bins=20, figsize=(12, 8))
plt.tight_layout()
plt.savefig('eda_histogram.png')
print("EDA visualization saved!")

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
print("Correlation heatmap saved!")
