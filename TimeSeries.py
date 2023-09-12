#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Load the dataset from a CSV file (replace with your file path)
data = pd.read_csv('Aquifer_Petrignano.csv')
# Remove rows with missing 'Rainfall_Bastia_Umbra' values
# Remove rows with missing 'Rainfall_Bastia_Umbra' values
data = data[data['Rainfall_Bastia_Umbra'].notna()]

# Drop unnecessary columns
data = data.drop(['Depth_to_Groundwater_P24', 'Temperature_Petrignano'], axis=1)

# Rename columns
data.columns = ['date', 'rainfall', 'depth_to_groundwater', 'temperature', 'drainage_volume', 'river_hydrometry']

# Convert 'date' column to datetime format
data['date'] = pd.to_datetime(data['date'], format='%d/%m/%Y')

# Display cleaned dataset
print(data.head())
print("Dataset shape:", data.shape)
print("Missing values:", data.isnull().sum())
print("Date range:", np.min(data['date']), "to", np.max(data['date']))


# In[14]:


# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Set up visualization style
sns.set_style('whitegrid')

# Plotting rainfall data over time
plt.figure(figsize=(14, 6))
plt.plot(data['date'], data['rainfall'], label='Rainfall', color='blue')
plt.title('Rainfall Over Time')
plt.xlabel('Date')
plt.ylabel('Rainfall (mm)')
plt.legend()
plt.show()


# In[15]:


# Plotting depth to groundwater over time
plt.figure(figsize=(14, 6))
plt.plot(data['date'], data['depth_to_groundwater'], label='Depth to Groundwater', color='green')
plt.title('Depth to Groundwater Over Time')S
plt.xlabel('Date')
plt.ylabel('Depth to Groundwater (m)')
plt.legend()
plt.show()


# In[16]:


# Plotting temperature data over time
plt.figure(figsize=(14, 6))
plt.plot(data['date'], data['temperature'], label='Temperature', color='red')
plt.title('Temperature Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.show()


# In[17]:


# Plotting drainage volume over time
plt.figure(figsize=(14, 6))
plt.plot(data['date'], data['drainage_volume'], label='Drainage Volume', color='purple')
plt.title('Drainage Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Drainage Volume')
plt.legend()
plt.show()


# In[18]:


# Plotting river hydrometry over time
plt.figure(figsize=(14, 6))
plt.plot(data['date'], data['river_hydrometry'], label='River Hydrometry', color='orange')
plt.title('River Hydrometry Over Time')
plt.xlabel('Date')
plt.ylabel('River Hydrometry')
plt.legend()
plt.show()


# In[24]:


# Import necessary libraries for time series decomposition and forecasting
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Handle missing values by forward filling
data['depth_to_groundwater'].fillna(method='ffill', inplace=True)

# Perform seasonal decomposition for depth to groundwater
decomposition = seasonal_decompose(data['depth_to_groundwater'], model='additive', period=365)
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid


# Plot the components of seasonal decomposition
plt.figure(figsize=(16, 12))

# Plot the components of seasonal decomposition
plt.figure(figsize=(16, 12))

plt.subplot(411)
plt.plot(data['date'], data['depth_to_groundwater'], label='Original')
plt.legend(loc='best')
plt.title('Original Data')

plt.subplot(412)
plt.plot(data['date'], trend, label='Trend', color='blue')
plt.legend(loc='best')
plt.title('Trend')

plt.subplot(413)
plt.plot(data['date'], seasonal, label='Seasonal', color='green')
plt.legend(loc='best')
plt.title('Seasonal')

plt.subplot(414)
plt.plot(data['date'], residual, label='Residual', color='red')
plt.legend(loc='best')
plt.title('Residual')

plt.tight_layout()
plt.show()


# In[28]:


# Handle missing values by forward filling
data['depth_to_groundwater'].fillna(method='ffill', inplace=True)

# Perform seasonal decomposition for depth to groundwater
decomposition = seasonal_decompose(data['depth_to_groundwater'], model='additive', period=365)
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

# Plot the components of seasonal decomposition
plt.figure(figsize=(16, 12))

plt.subplot(411)
plt.plot(data['date'], data['depth_to_groundwater'], label='Original')
plt.legend(loc='best')
plt.title('Original Data')


# In[29]:



# Plot autocorrelation and partial autocorrelation plots
plt.figure(figsize=(12, 6))

plot_acf(data['depth_to_groundwater'], lags=30, ax=plt.gca(), title='Autocorrelation')
plot_pacf(data['depth_to_groundwater'], lags=30, ax=plt.gca(), title='Partial Autocorrelation')

plt.show()


# In[22]:


# Apply moving average for rainfall and depth to groundwater
data['rainfall_rolling_mean'] = data['rainfall'].rolling(window=30).mean()
data['depth_to_groundwater_rolling_mean'] = data['depth_to_groundwater'].rolling(window=30).mean()

# Plot smoothed rainfall and depth to groundwater
plt.figure(figsize=(14, 6))
plt.plot(data['date'], data['rainfall'], label='Rainfall', color='blue', alpha=0.5)
plt.plot(data['date'], data['rainfall_rolling_mean'], label='Rainfall (30-day Rolling Mean)', color='red')
plt.plot(data['date'], data['depth_to_groundwater'], label='Depth to Groundwater', color='green', alpha=0.5)
plt.plot(data['date'], data['depth_to_groundwater_rolling_mean'], label='Depth to Groundwater (30-day Rolling Mean)', color='purple')
plt.title('Smoothed Rainfall and Depth to Groundwater')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()


# In[23]:


# Calculate and visualize correlations
correlation_matrix = data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap')
plt.show()


# In[ ]:




