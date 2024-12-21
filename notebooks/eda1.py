#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv(r"C:\Users\hp\Desktop\New folder\Kifya AIM Training Program\data\benin-malanville.csv")
print(df.head())  # Print the first 5 rows instead of the entire DataFrame


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Check the shape of the dataset
print(f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

# Display column names and data types
print(df.info())

# Summary statistics
print(df.describe())


# In[3]:


# Check for missing values
print(df.isnull().sum())

# Handle missing values (example: filling or dropping)
df = df.dropna()  # Dropping rows with missing values
# Alternatively: df.fillna(value, inplace=True)


# In[4]:


# Check for duplicates
duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

# Remove duplicates if needed
df = df.drop_duplicates()


# In[5]:


# Display unique values and their counts
print(df['Timestamp'].value_counts())

# Plot the distribution
sns.countplot(data=df, x='Timestamp')
plt.show()


# In[6]:


# Histogram and KDE plot
df['GHI'].hist(bins=20, edgecolor='k')
plt.title('Histogram')
plt.show()

sns.kdeplot(data=df, x='GHI', shade=True)
plt.title('KDE Plot')
plt.show()


# In[7]:


# Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()


# In[9]:


# Convert to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Plot time-series data
df.set_index('Timestamp')['GHI'].plot()
plt.title('Time Series Plot')
plt.show()


# In[ ]:




