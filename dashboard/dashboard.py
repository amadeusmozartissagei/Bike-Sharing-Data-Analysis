# File: bike_sharing_dashboard.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np
import os
from datetime import datetime

# Set a modern, vibrant plot style
sns.set(style='whitegrid')

# Using absolute path for data location
current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, "main_data.csv")

# Load datasets
day_df = pd.read_csv(data_path)

# Data preprocessing
day_df.rename(columns={
    'dteday': 'dateday',
    'yr': 'year',
    'mnth': 'month',
    'weathersit': 'weather',
    'cnt': 'count'
}, inplace=True)

day_df['month'] = day_df['month'].map({
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
})
day_df['season'] = day_df['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})
day_df['weather'] = day_df['weather'].map({
    1: 'Clear/Partly Cloudy',
    2: 'Misty/Cloudy',
    3: 'Light Snow/Rain',
    4: 'Severe Weather'
})

# Convert 'dateday' to datetime
day_df['dateday'] = pd.to_datetime(day_df['dateday'])
day_df['season'] = day_df['season'].astype('category')
day_df['year'] = day_df['year'].astype('category')
day_df['month'] = day_df['month'].astype('category')
day_df['weather'] = day_df['weather'].astype('category')

# RFM Analysis
latest_date = day_df['dateday'].max()
day_df['days_since_last_rental'] = (latest_date - day_df['dateday']).dt.days

# Frequency (rentals per month)
day_df['month_year'] = day_df['dateday'].dt.to_period('M')
frequency_df = day_df.groupby('month_year')['count'].count().reset_index()

# Monetary (total rentals per day)
monetary_df = day_df.groupby('dateday')['count'].sum().reset_index()

# Combine RFM data
rfm_df = day_df[['dateday', 'days_since_last_rental', 'count']].copy()
rfm_df = rfm_df.groupby('dateday').agg({
    'days_since_last_rental': 'min',
    'count': ['sum', 'count']
}).reset_index()

rfm_df.columns = ['dateday', 'recency', 'monetary', 'frequency']

# Streamlit Dashboard
st.title("Bike Sharing Data Analysis Dashboard")

# Sidebar Information
st.sidebar.title("Information")
st.sidebar.write("Select the date range to filter the data displayed on the dashboard.")

# Filter for date range
min_date = day_df['dateday'].min().date()
max_date = day_df['dateday'].max().date()

try:
    start_date, end_date = st.sidebar.date_input(
        "Select Date Range",
        [min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

    # Apply date filter only if both dates are selected
    if start_date and end_date:
        filtered_df = day_df[(day_df['dateday'] >= str(start_date)) & (day_df['dateday'] <= str(end_date))]
    else:
        filtered_df = day_df  # If dates are not selected, show the entire dataset

except ValueError:
    st.sidebar.warning("Please select a valid date range.")
    filtered_df = day_df  # Fallback to the entire dataset in case of invalid input

# Display basic statistics
st.header("Basic Statistics")
st.write(filtered_df.describe())

# Total Rental by Season
st.subheader("Total Rentals by Season")
season_usage = filtered_df.groupby('season')['count'].sum().reset_index()

fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x='season', y='count', data=season_usage, palette='Spectral', ax=ax)  # Updated palette
ax.set_title('Total Bike Rentals by Season', fontsize=14, fontweight='bold')
ax.set_xlabel('Season', fontsize=12)
ax.set_ylabel('Total Rentals', fontsize=12)
st.pyplot(fig)

# Rentals by Weather Condition
st.subheader("Rentals by Weather Condition")
fig, ax = plt.subplots(figsize=(8, 6))
sns.boxplot(x='weather', y='count', data=filtered_df, palette='coolwarm', ax=ax)  # Updated palette
ax.set_title('Box Plot: Weather vs Bike Rentals', fontsize=14, fontweight='bold')
ax.set_xlabel('Weather Condition', fontsize=12)
ax.set_ylabel('Total Rentals', fontsize=12)
st.pyplot(fig)

# Order months for visualization
month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
day_df['month'] = pd.Categorical(day_df['month'], categories=month_order, ordered=True)

# Group and calculate average bike usage per month for each year
monthly_usage = day_df.groupby(['year', 'month'])['count'].mean().unstack()

fig, ax = plt.subplots(figsize=(10, 6))
monthly_usage.T.plot(kind='line', marker='o', linestyle='-', colormap='tab10', ax=ax)  # Updated color map
ax.set_title('Average Monthly Bike Rentals (2011 vs 2012)', fontsize=14, fontweight='bold')
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Average Rentals', fontsize=12)
ax.set_xticks(range(12))
ax.set_xticklabels(monthly_usage.columns, rotation=45)
ax.legend(title='Year')
st.pyplot(fig)

# RFM Analysis Visualization
st.subheader("RFM Analysis: Recency vs Monetary vs Frequency")

fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(rfm_df['recency'], rfm_df['monetary'], c=rfm_df['frequency'], cmap='plasma', s=100, alpha=0.7)  # Updated color map
plt.colorbar(scatter, ax=ax, label='Frequency')
ax.set_title('RFM Analysis: Recency vs Monetary vs Frequency', fontsize=14, fontweight='bold')
ax.set_xlabel('Recency (Days Since Last Rental)', fontsize=12)
ax.set_ylabel('Monetary (Total Rentals)', fontsize=12)
st.pyplot(fig)

# Copyright Information
st.sidebar.markdown("---")
st.sidebar.text("© 2024 Hamza Pratama")
st.sidebar.text("Name: Hamza Pratama")
st.sidebar.text("Email: hamzapratama000@gmail.com")
st.sidebar.text("ID Dicoding: hamzaapratama")