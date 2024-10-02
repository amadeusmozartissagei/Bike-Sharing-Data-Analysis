# dashboard/dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
day_df = pd.read_csv('data/day.csv')
hour_df = pd.read_csv('data/hour.csv')

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
