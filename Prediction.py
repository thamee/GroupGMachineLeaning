import os
import datetime

import IPython
import IPython.display
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf

mpl.rcParams['figure.figsize'] = (8, 6)
mpl.rcParams['axes.grid'] = False
df = pd.read_csv('AzureUsageData.csv') 
# Slice [start:stop:step], starting from index 5 take every 6th record.
df = df[5::6]

df['Date'] = pd.to_datetime(df.pop('Date'), format='%m/%d/%Y' )
df['Date'] = (df['Date'] - df['Date'].min()).dt.days
from sklearn.linear_model import LinearRegression

# Make prediction for the future date
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Assuming `df` is your DataFrame
le = LabelEncoder()
scaler = MinMaxScaler()

# Encode categorical variables
for col in ['SubscriptionName', 'SubscriptionGuid', 'ResourceGuid', 'ServiceName', 'ServiceType', 'ServiceRegion', 'ServiceResource']:
    df[col] = le.fit_transform(df[col])

# Normalize numerical variables
for col in ['Quantity']:
    df[col] = scaler.fit_transform(df[col].values.reshape(-1, 1))

# Convert 'Date' to datetime and create a 'Day' feature
df['Date'] = pd.to_datetime(df['Date'])
df['Day'] = (df['Date'] - df['Date'].min()).dt.days

# Split the data into training and testing sets
X = df.drop(['Cost', 'Date'], axis=1)
y = df['Cost']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)  # or mse**(0.5)  
r2 = r2_score(y_test, y_pred)

print('Mean Absolute Error:', mae)
print('Mean Squared Error:', mse)
print('Root Mean Squared Error:', rmse)
print('R-squared:', r2)
# Print coefficients
