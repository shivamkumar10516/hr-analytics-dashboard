# src/metrics.py
import pandas as pd

def calculate_core_kpis(df: pd.DataFrame) -> dict:
    """
    Computes key performance indicators for HR management decision making.
    """
    if df.empty:
        return {"total_emp": 0, "attrition_rate": 0.0, "avg_salary": 0.0, "avg_exp": 0.0}
        
    total_employees = len(df)
    
    # Calculate Attrition Rate (%)
    attrition_count = len(df[df['Attrition'] == 'Yes'])
    attrition_rate = (attrition_count / total_employees) * 100 if total_employees > 0 else 0.0
    
    # Financials and Tenure
    avg_salary = df['Monthly_Income'].mean()
    avg_experience = df['Total_Working_Years'].mean()
    
    return {
        "total_emp": total_employees,
        "attrition_rate": round(attrition_rate, 1),
        "avg_salary": round(avg_salary, 2),
        "avg_exp": round(avg_experience, 1)
    }
