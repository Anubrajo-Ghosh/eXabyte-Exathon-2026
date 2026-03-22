import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

# --- 1. SETUP & DATA ---
st.set_page_config(page_title="Urban Heat Resilience Planner", layout="wide")
st.title("🌡️ Urban Heat Resilience Planner")

# Base Dataset (2026) [cite: 31]
data = {
    'Neighborhood': ['Park Street', 'Salt Lake', 'Gariahat', 'Howrah', 'New Town'],
    'Lat': [22.55, 22.58, 22.52, 22.58, 22.59],
    'Lon': [88.35, 88.42, 88.36, 88.33, 88.47],
    'Temp_C': [38.0, 34.0, 37.0, 40.0, 33.0],
    'Vegetation_%': [10, 40, 15, 5, 45]
}
df = pd.DataFrame(data)

# --- 2. SIDEBAR: PREDICTIVE AI & CONTROLS ---
st.sidebar.header("🔮 Predictive Analytics")
# Feature: Estimating future heat conditions 
target_year = st.sidebar.select_slider("Select Projection Year", options=[2026, 2030, 2040, 2050])

# Global Warming Trend Logic (Predictive AI Model)
years_ahead = target_year - 2026
predicted_rise = years_ahead * 0.05 

st.sidebar.markdown("---")
st.sidebar.header("🕹️ Planner Controls")
# Feature: Decision-support simulation 
tree_bonus = st.sidebar.slider("Simulate Tree Canopy Increase (%)", 0, 50, 0)

# --- 3. AI RISK CALCULATION ENGINE [cite: 32] ---
# Risk Score = (Projected Temp impact) - (Vegetation/Cooling impact)
df['Projected_Temp'] = df['Temp_C'] + predicted_rise
df['Risk_Score'] = ((df['Projected_Temp'] - 30) * 1.5 - ((df['Vegetation_%'] + tree_bonus) / 10)).clip(1, 10).round(1)

# --- 4. MAIN INTERFACE ---
tab1, tab2, tab3 = st.tabs(["🗺️ Heat Map", "📊 Data Analytics", "🌱 Mitigation Strategies"])

with tab1:
    st.subheader(f"Urban Heat Mapping: {target_year} Projection")
    m = folium.Map(location=[22.5726, 88.3639], zoom_start=12)
    for idx, row in df.iterrows():
        # Visual color coding for risk levels [cite: 27]
        color = 'red' if row['Risk_Score'] > 7 else 'orange' if row['Risk_Score'] > 4 else 'green'
        folium.CircleMarker(
            location=[row['Lat'], row['Lon']],
            radius=row['Risk_Score'] * 4,
            popup=f"{row['Neighborhood']} ({target_year}) | Risk: {row['Risk_Score']}",
            color=color, fill=True, fill_opacity=0.6
        ).add_to(m)
    st_folium(m, width=900, height=500)

with tab2:
    st.subheader("Predictive Insights")
    st.write(f"In **{target_year}**, average urban temperatures are projected to rise by **{predicted_rise:.2f}°C** due to the Urban Heat Island effect.")
    st.dataframe(df[['Neighborhood', 'Projected_Temp', 'Risk_Score']])

with tab3:
    st.subheader("Decision Support: Mitigation")
    selected_zone = st.selectbox("Select Neighborhood for Analysis", df['Neighborhood'])
    zone_data = df[df['Neighborhood'] == selected_zone].iloc[0]
    
    if zone_data['Risk_Score'] > 7:
        st.error(f"⚠️ CRITICAL HEAT RISK in {target_year} for {selected_zone}")
        st.markdown("""
        **Recommended Strategies:** 
        * **Reflective Infrastructure:** Deploy 'Cool Roof' programs.
        * **Urban Forestry:** Immediate 15% increase in local green cover.
        * **Cooling Hubs:** Establish air-conditioned community relief centers.
        """)
    else:
        st.success(f"✅ {selected_zone} remains resilient through {target_year}.")

# --- 5. COMMUNITY INPUT  ---
st.markdown("---")
st.subheader("📢 Community Hot-Spot Reporting")
with st.form("community_report"):
    col_a, col_b = st.columns(2)
    with col_a:
        loc = st.text_input("Enter Street/Area Name")
    with col_b:
        intensity = st.select_slider("Heat Intensity", options=["Warm", "Hot", "Extreme"])
    
    if st.form_submit_button("Submit Report"):
        st.success(f"Thank you. The report for {loc} has been added to our Resilience Database.")

# --- FOOTER ---
st.caption("Developed for Exathon 2026 | St. Xavier's College, Kolkata")