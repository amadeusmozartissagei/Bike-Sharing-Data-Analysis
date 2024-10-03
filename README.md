

## Project: Bike Sharing Data Analysis

### Overview
This project analyzes the bike-sharing dataset, focusing on various factors that affect bike rental patterns, such as weather conditions, seasons, and daily/hourly trends. The analysis is performed using **Streamlit** for an interactive dashboard and **Jupyter Notebook** for in-depth data exploration.

### Features
1. **Streamlit Dashboard** (`dashboard.py`)
   - Visualizes the impact of weather conditions on bike rentals across different seasons.
   - Displays hourly rental trends based on weekdays and holidays.
   - **New Feature**: Added data cleaning steps, including:
     - Checking for missing values.
     - Checking for duplicate entries.
     - Descriptive statistics to summarize the dataset.
   - **New Feature**: Aggregation of user count by season, providing insights into rental patterns during different seasons.

2. **Jupyter Notebook** (`notebook.ipynb`)
   - Performs detailed exploratory data analysis (EDA).
   - **New Feature**: Added sections for:
     - Missing value detection.
     - Duplicate row detection.
     - Descriptive statistics for both daily and hourly datasets.
   - **New Feature**: Aggregates total bike rentals based on seasons and months.
   - Visualizations include bar charts and line plots to present the insights.

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/amadeusmozartissagei/Bike-Sharing-Data-Analysis.git
   ```

2. **Install dependencies**:
   Ensure you have all the required Python packages installed by running:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit dashboard**:
   Navigate to the project directory and run:
   ```bash
   streamlit run dashboard.py
   ```

4. **Explore the Jupyter Notebook**:
   Open the notebook using Jupyter:
   ```bash
   jupyter notebook notebook.ipynb
   ```

### Dependencies
All dependencies are listed in the `requirements.txt` file. Main libraries used:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `streamlit`


---

### © Copyright

- **Name:** Hamza Pratama
- **Email:** [hamzapratama000@gmail.com](mailto:hamzapratama000@gmail.com)
- **ID Dicoding:** hamzaapratama
