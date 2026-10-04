# app.py
import streamlit as st
from data.mock_data_generator import generate_hr_dataset
from src.metrics import calculate_core_kpis
from src.ui_components import render_custom_css, display_metric_card

# Initialize page settings
st.set_page_config(page_title="Corporate HR Insights Platform", layout="wide")

# Inject our unique custom styles
render_custom_css()

# App Header
st.title("Workforce Analytics Portal")
st.markdown("Real-time executive overview of organizational metrics and attrition dynamics.")
st.markdown("---")

# Load operational dataset
@st.cache_data
def load_dashboard_data():
    return generate_hr_dataset(num_employees=300)

df_hr = load_dashboard_data()

# Sidebar department filter (adds premium functionality)
st.sidebar.header("Dashboard Filters")
selected_dept = st.sidebar.multiselect(
    "Filter by Department",
    options=list(df_hr['Department'].unique()),
    default=list(df_hr['Department'].unique())
)

# Filter dataset dynamically based on selection
filtered_df = df_hr[df_hr['Department'].isin(selected_dept)]

# Run calculations through modular math layer
kpis = calculate_core_kpis(filtered_df)

# Create 4 columns for your specific requested KPIs
col1, col2, col3, col4 = st.columns(4)

with col1:
    display_metric_card("Total Employees", f"{kpis['total_emp']}")

with col2:
    display_metric_card("Attrition Rate", f"{kpis['attrition_rate']}%")

with col3:
    display_metric_card("Average Salary", f"₹{kpis['avg_salary']:,.2f}")

with col4:
    display_metric_card("Avg Experience", f"{kpis['avg_exp']} Years")

# Showcase raw data below metrics for corporate transparency
st.markdown("<br><br>", unsafe_allow_html=True)
st.subheader("Active Workforce Roster")
st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)
