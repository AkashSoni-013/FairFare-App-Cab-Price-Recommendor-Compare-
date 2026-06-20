# 🚖 FairFare App - Smart Cab Price Recommendation System

Built a data-driven web application using Streamlit that compares prices of three different cab services for the same route, date, and time. The app recommends the cheapest and most cost-effective option to customers, helping them make smarter travel decisions.
Key Highlights:

Designed and implemented the data pipeline to fetch, clean, and process cab fare data.

Applied data science techniques to standardize pricing and ensure fair comparisons.

Developed an interactive Streamlit app for real-time price comparison and recommendation.

Created Tableau dashboards to visualize cab fare trends, pricing patterns, and customer savings insights.

Delivered a solution that combines analytics + user-friendly design to enhance customer decision-making.


 # Introduction
# FairFare is an intelligent cab fare comparison system built to help users choose the most affordable
cab among Ola, Uber and Rapido using historical data.

# Problem Statement
"I noticed that cab prices vary significantly across platforms for the same route. Users often switch between apps to compare prices manually. I wanted to create a solution that analyzes pricing patterns and recommends the best option quickly."

Users manually compare multiple apps and face unpredictable surge pricing, wasting time and
money.
# Objectives
To provide a centralized system that automatically compares cab prices and recommends the
cheapest option based on route and time.

# System Architecture
Data Collection → Cleaning → Feature Engineering → Recommendation Engine → Streamlit
Interface

# Technologies Used
Python, Pandas, Streamlit, Datetime, Feature Engineering, Caching.

# Data Pipeline
Data was collected from Kaggle and open sources. Cleaning removed duplicates, nulls,
standardized time formats and selected relevant features.

# Recommendation Logic
Closest hour matching is applied to recommend the cheapest cab using actual historical fare
values.

# User Interface
Streamlit-based interface allows easy selection of pickup, destination and time, providing instant
recommendations.

# Challenges Faced
Handling inconsistent time, missing data, performance issues, route duplication and UI
responsiveness.

# Future Enhancements
Live APIs, surge forecasting ML models, GPS-based location detection, mobile app integration.

# Conclusion
FairFare demonstrates real-world data engineering, ML logic and deployment skills in one product.


