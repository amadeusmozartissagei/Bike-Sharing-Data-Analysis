# dashboard/dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Get the current directory path (which is the location of dashboard.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the data files in the 'data' directory (one level up)
data_1_path = os.path.join(current_dir, '..', 'data', 'day.csv')
data_2_path = os.path.join(current_dir, '..', 'data', 'hour.csv')

# Debugging: Print the paths to verify if they are correct (will be visible only in the terminal/console)
print("Path to data_1.csv:", os.path.abspath(data_1_path))
print("Path to data_2.csv:", os.path.abspath(data_2_path))

# Verify if the files exist
if not os.path.exists(data_1_path):
    st.error(f"Error: The file at {os.path.abspath(data_1_path)} does not exist.")
if not os.path.exists(data_2_path):
    st.error(f"Error: The file at {os.path.abspath(data_2_path)} does not exist.")

# Load datasets if they exist
if os.path.exists(data_1_path) and os.path.exists(data_2_path):
    day_df = pd.read_csv(data_1_path)
    hour_df = pd.read_csv(data_2_path)

    # Streamlit App Configuration
    st.title("Bike Sharing Data Analysis")
    st.sidebar.title("Filters")

    # Weather and Season Analysis
    st.header("Impact of Weather on Bike Rentals Across Seasons")
    weather_filter = st.sidebar.selectbox("Select Season", day_df['season'].unique())
    filtered_data = day_df[day_df['season'] == weather_filter]

    fig, ax = plt.subplots()
    sns.barplot(x='weathersit', y='cnt', data=filtered_data, ax=ax, ci=None)
    st.pyplot(fig)

    # Hourly Trend Analysis
    st.header("Bike Rentals by Hour of the Day for Weekdays and Holidays")
    day_filter = st.sidebar.selectbox("Select Weekday", hour_df['weekday'].unique())
    filtered_hour = hour_df[hour_df['weekday'] == day_filter]

    fig2, ax2 = plt.subplots()
    sns.lineplot(x='hr', y='cnt', data=filtered_hour, ax=ax2)
    st.pyplot(fig2)

    # Summary Insights
    st.markdown("## Insights")
    st.markdown("""
    - Different weather situations have varying impacts on the number of bike rentals, especially across different seasons.
    - Weekdays and weekends show different trends in rental usage, highlighting specific hours with higher activity.
    """)

# Copyright Information
st.sidebar.markdown("---")
st.sidebar.markdown("### © Copyright")
st.sidebar.markdown("""
- **Name:** Hamza Pratama
- **Email:** [hamzapratama000@gmail.com](mailto:hamzapratama000@gmail.com)
- **ID Dicoding:** hamzaapratama
""")

# Alternatively, add copyright information at the bottom of the main page
st.markdown("---")
st.markdown("""
### © Copyright
- **Name:** Hamza Pratama
- **Email:** [hamzapratama000@gmail.com](mailto:hamzapratama000@gmail.com)
- **ID Dicoding:** hamzaapratama
""")
