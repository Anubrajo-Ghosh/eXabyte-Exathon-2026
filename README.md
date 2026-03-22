# Lumina: Urban Heat Resilience Planner 🌡️
## **eXabyte Exathon 2026** </br>
**Track 2: Climate & Urban Future** </br> 
**Event: Exathon 2026 | St. Xavier's College (Autonomous), Kolkata 📖** 

## Project Overview:-
Lumina is a digital decision-support tool designed to help city planners and citizens combat the Urban Heat Island (UHI) effect. As urban temperatures rise due to dense infrastructure and lack of vegetation, Lumina provides a data-driven roadmap to identify high-risk zones and simulate cooling interventions.

## Core Problems Solved:
* Information Overload: Consolidates temperature and vegetation data into a single visual interface.
* Lack of Foresight: Uses predictive analytics to estimate heat risks up to the year 2050.
* Actionable Gap: Recommends specific mitigation strategies (Cool Roofs, Urban Forestry) based on local risk scores.

## ✨ Key Features:-
* Interactive Heat Mapping: Visualizes neighborhood-wise vulnerability using color-coded risk indicators.
* Predictive AI Engine: Estimates future heat conditions based on current climate trends and urban density.
* "What-If" Planning Simulator: Allows users to virtually "add" tree canopy and see the real-time impact on the Heat Risk Index.
* Community Reporting: A crowdsourced feature for citizens to report local "hot spots" for hyper-local monitoring.

## 🧬 The Lumina HRI Algorithm
* We developed a custom Heat Risk Index (HRI) to quantify urban vulnerability:
* **HRI = [(Projected Temp - 30) * 1.5] - [(Vegetation % + Simulated Trees) / 10]**
* The Logic: We use 30°C as a baseline for urban comfort. Risk increases with projected temperature rise and decreases as vegetation/cooling infrastructure is added.

## 🛠️ Tech Stack 
* Programming language: **Python 3.x**
* Web Framework: **Streamlit** (For the visual dashboard) 
* Geospatial Engine: **Folium** (For interactive mapping) 
* Data Processing: **Pandas** (For risk score calculations and dataset management) 

## 🚀 How to Run Locally
* Install Dependencies: **Bash** pip install streamlit folium streamlit-folium pandas
* Launch the Application: **Bash** streamlit run app.py
* Access the Dashboard: Open the URL provided in the terminal (usually http://localhost:8501).

## 👥 Team 
Developed by Binary Biologists </br>
1st Year MCBA, St. Xavier's College, Kolkata.
