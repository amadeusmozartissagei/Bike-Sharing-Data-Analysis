# dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Set up the dashboard title
st.title("RFM Analysis Dashboard with Business Questions")

# Load the dataset (replace with actual data path or data loading logic)
@st.cache_data
def load_data():
    # Example dataset, replace this with actual RFM dataset
    data = pd.DataFrame({
        'recency': [10, 20, 30, 40],
        'monetary': [100, 200, 300, 400],
        'frequency': [1, 2, 3, 4],
        'date': pd.to_datetime(['2023-01-10', '2023-02-20', '2023-03-30', '2023-04-10'])  # example dates
    })
    return data

# Load the data
rfm_df = load_data()

# Display the full dataset
st.subheader("Full RFM Dataset")
st.write(rfm_df)  # Display all data

# Business Questions Section
st.subheader("Business Questions")
business_questions = """
1. What are the conditions of bike rentals based on the season in the past two years?
2. Is there a correlation between weather conditions and the number of bike rentals per day?
3. What is the trend of bike usage over one year, and is the usage higher in 2011 or 2012?
"""
st.markdown(business_questions)

# Date filter
st.subheader("Filter by Date")
start_date = st.date_input("Start date", datetime.date(2023, 1, 1))
end_date = st.date_input("End date", datetime.date(2023, 12, 31))

# Filter the dataset based on selected dates
filtered_df = rfm_df[(rfm_df['date'] >= pd.to_datetime(start_date)) & (rfm_df['date'] <= pd.to_datetime(end_date))]

# Display the filtered data
st.subheader("Filtered Data")
st.write(filtered_df)

# Create a scatter plot for RFM analysis
st.subheader("RFM Analysis: Recency vs Monetary vs Frequency (Filtered)")

fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(filtered_df['recency'], filtered_df['monetary'], c=filtered_df['frequency'], cmap='viridis', s=100, alpha=0.7)
plt.colorbar(scatter, ax=ax, label='Frequency')
ax.set_title('Recency vs Monetary vs Frequency (Filtered by Date)')
ax.set_xlabel('Recency (Days since last rental)')
ax.set_ylabel('Monetary (Total Rentals)')
ax.grid(True)

# Display the plot in Streamlit
st.pyplot(fig)

# Conclusion section
st.subheader("Conclusion")

conclusions = """
- The best times to increase bike rentals are during the autumn and summer seasons, while specific strategies may be needed to boost usage during spring.
- Bike rental services tend to be most popular when the weather is good, such as sunny or cloudy conditions.
- September 2012 marks a significant peak in usage, indicating that promotional efforts during this period could enhance rentals.
"""

st.markdown(conclusions)

# Copyright section
st.subheader("© Copyright")
st.markdown("""
**Name**: Hamza Pratama  
**Email**: hamzapratama000@gmail.com  
**ID Dicoding**: hamzaapratama
""")
