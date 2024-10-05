import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set up the dashboard title
st.title("RFM Analysis Dashboard with Bike Sharing Visualizations")

# Cache the data loading function to optimize performance
@st.cache_data
def load_rfm_data():
    # Example RFM dataset (replace this with your actual RFM data loading logic)
    data = pd.DataFrame({
        'recency': [10, 20, 30, 40],
        'monetary': [100, 200, 300, 400],
        'frequency': [1, 2, 3, 4]
    })
    return data

# Load your RFM data
rfm_data = load_rfm_data()

# Display the RFM data in the dashboard
st.subheader("RFM Analysis Data")
st.write(rfm_data)

# Cache the bike-sharing data loading function
@st.cache_data
def load_bike_data():
    np.random.seed(42)
    # Generate data for two years, 2011 and 2012
    dates = pd.date_range(start="2011-01-01", end="2012-12-31", freq='D')
    n = len(dates)
    
    # Sample data fields
    data = {
        'date': dates,
        'season': np.random.choice(['Spring', 'Summer', 'Fall', 'Winter'], n),
        'weather': np.random.choice(['Clear', 'Cloudy', 'Rainy', 'Snowy'], n),
        'bike_rentals': np.random.poisson(lam=200, size=n),
    }

    df = pd.DataFrame(data)
    
    # Adjust some patterns to simulate seasonal effects
    df.loc[df['season'] == 'Winter', 'bike_rentals'] = df.loc[df['season'] == 'Winter', 'bike_rentals'] * 0.5
    df.loc[df['season'] == 'Summer', 'bike_rentals'] = df.loc[df['season'] == 'Summer', 'bike_rentals'] * 1.5
    
    return df

# Load the bike-sharing data
bike_data = load_bike_data()

# Sidebar for filtering bike-sharing data
st.sidebar.header("Bike Sharing Filters")
year_selected = st.sidebar.slider('Select Year', 2011, 2012, (2011, 2012))
season_selected = st.sidebar.multiselect('Select Seasons', options=['Spring', 'Summer', 'Fall', 'Winter'], default=['Spring', 'Summer', 'Fall', 'Winter'])
weather_selected = st.sidebar.multiselect('Select Weather Conditions', options=['Clear', 'Cloudy', 'Rainy', 'Snowy'], default=['Clear', 'Cloudy', 'Rainy', 'Snowy'])

# Filter bike-sharing data based on the sidebar selections
filtered_bike_data = bike_data[(bike_data['date'].dt.year >= year_selected[0]) & (bike_data['date'].dt.year <= year_selected[1])]
filtered_bike_data = filtered_bike_data[filtered_bike_data['season'].isin(season_selected)]
filtered_bike_data = filtered_bike_data[filtered_bike_data['weather'].isin(weather_selected)]

# Display the filtered bike-sharing data
st.subheader(f"Bike Sharing Data (from {year_selected[0]} to {year_selected[1]})")
st.write(filtered_bike_data.head())

# Visualization 1: Bike Rentals by Season
st.subheader("Bike Rentals by Season")
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.boxplot(data=filtered_bike_data, x='season', y='bike_rentals', palette='coolwarm', ax=ax1)
ax1.set_title("Bike Rentals by Season (2011-2012)")
ax1.set_xlabel("Season")
ax1.set_ylabel("Number of Bike Rentals")
st.pyplot(fig1)

# Visualization 2: Bike Rentals by Weather Conditions
st.subheader("Bike Rentals by Weather Conditions")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.boxplot(data=filtered_bike_data, x='weather', y='bike_rentals', palette='Blues', ax=ax2)
ax2.set_title("Bike Rentals by Weather Conditions (2011-2012)")
ax2.set_xlabel("Weather Condition")
ax2.set_ylabel("Number of Bike Rentals")
st.pyplot(fig2)


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
