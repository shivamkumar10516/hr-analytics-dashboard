# src/ui_components.py
import streamlit as st

def render_custom_css():
    """Injects bespoke minimalist CSS for a sleek executive dashboard layout."""
    st.markdown("""
        <style>
            .kpi-container {
                background-color: #f8f9fa;
                border: 1px solid #e9ecef;
                padding: 1.25rem;
                border-radius: 8px;
                text-align: center;
                box-shadow: 0 2px 4px rgba(0,0,0,0.02);
            }
            .kpi-label {
                font-size: 0.85rem;
                color: #6c757d;
                text-transform: uppercase;
                letter-spacing: 0.5px;
                font-weight: 600;
                margin-bottom: 0.5rem;
            }
            .kpi-value {
                font-size: 1.85rem;
                color: #212529;
                font-weight: 700;
            }
        </style>
    """, unsafe_allow_html=True)

def display_metric_card(label: str, value: str):
    """Renders a beautifully styled human-designed KPI card."""
    st.markdown(f"""
        <div class="kpi-container">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
        </div>
    """, unsafe_allow_html=True)
