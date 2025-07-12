import streamlit as st
import pandas as pd
from datetime import datetime

# Load and preprocess data
@st.cache_data
def load_data():
    df = pd.read_csv('cab_price.csv')
    # Convert time to datetime and extract hour
    df['Time'] = pd.to_datetime(df['Time of Day'], errors='coerce')
    df['Hour'] = df['Time'].dt.hour
    return df

df = load_data()

# UI Setup
st.set_page_config(page_title="Cab Price Comparator", layout="wide")
st.title("🚖 Cab Price Comparison Tool")
st.subheader("Compare Ola Mini    vs    Rapido Car    vs    Uber Go")

# User Inputs
col1, col2 = st.columns(2)
with col1:
    pickup = st.selectbox("Pickup Location", 
                        sorted(df['Pickup Location'].unique()),
                        help="Where are you starting your trip?")

with col2:
    destination = st.selectbox("Destination", 
                             sorted(df['Destination'].unique()),
                             help="Where are you going?")

current_hour = st.slider("Current Hour", 0, 23, datetime.now().hour)

# Filter data based on user inputs
def get_recommendation(df, pickup, destination, hour):
    # Filter routes
    route_df = df[(df['Pickup Location'] == pickup) & 
                 (df['Destination'] == destination)].copy()
    
    if route_df.empty:
        return None, None
    
    # Get closest time match (within 2 hours)
    route_df['Time Diff'] = abs(route_df['Hour'] - hour)
    closest_time = route_df.sort_values('Time Diff').iloc[0]
    
    # Compare the 3 services
    services = {
        'Ola Mini': closest_time['Ola Mini'],
        'Rapido Car': closest_time['Rapido Car'],
        'Uber Go': closest_time['Uber Go']
    }
    
    # Find cheapest
    cheapest_service = min(services, key=services.get)
    cheapest_price = services[cheapest_service]
    
    return services, (cheapest_service, cheapest_price)

# When user clicks compare
if st.button("Find Cheapest Cab", type="primary"):
    services, cheapest = get_recommendation(df, pickup, destination, current_hour)
    
    if not services:
        st.error("No routes found between these locations")
    else:
        st.subheader("💰 Price Comparison")
        
        # Create comparison table
        comparison_df = pd.DataFrame({
            'Service': list(services.keys()),
            'Price (₹)': list(services.values())
        })
        
        # Highlight cheapest option
        def highlight_cheapest(row):
            return ['background-color: lightgreen' if row['Service'] == cheapest[0] else '' for _ in row]
        
        st.dataframe(
            comparison_df.style.apply(highlight_cheapest, axis=1),
            hide_index=True,
            use_container_width=True
        )
        
        # best recommendation at that time 
        st.success(f"**Best Option:** {cheapest[0]} at ₹{cheapest[1]}")
        
        # Additional info
        st.write(f"**Time Considered:** {current_hour}:00")
        st.write(f"**Route:** {pickup} → {destination}")

#  some explanations for new Customer
with st.expander("How this works"):
    st.write("""
    1. We match your pickup and destination with our database
    2. Find the closest recorded time to your selected hour
    3. Compare prices for Ola Mini, Rapido Car, and Uber Go
    4. Recommend the cheapest option with actual fare data
    """)
    st.write("Data last updated: " + str(df['Time'].max().date()))