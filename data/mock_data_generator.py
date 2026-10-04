# data/mock_data_generator.py
import pandas as pd
import numpy as np

def generate_hr_dataset(num_employees=250):
    """
    Generates a highly realistic corporate HR dataset for analytics testing.
    """
    np.random.seed(42)  # Ensures consistent data across runs
    
    departments = ['Engineering', 'Sales', 'Marketing', 'HR', 'Finance']
    education_fields = ['Life Sciences', 'Medical', 'Marketing', 'Technical Degree', 'Other']
    genders = ['Female', 'Male']
    
    # 1. Pehle baaki saara data generate karte hain jinka size same hai
    data = {
        'Employee_ID': [f"EMP-{1000 + i}" for i in range(num_employees)],
        'Age': np.random.randint(22, 60, size=num_employees),
        'Gender': np.random.choice(genders, size=num_employees, p=[0.45, 0.55]),
        'Department': np.random.choice(departments, size=num_employees),
        'Education_Field': np.random.choice(education_fields, size=num_employees),
        'Total_Working_Years': np.random.randint(1, 20, size=num_employees),
        'Monthly_Income': np.random.randint(45000, 185000, size=num_employees)
    }
    
    df = pd.DataFrame(data)
    
    # 2. Ab logic ke hisab se attrition list banate hain
    attrition_list = []
    for _, row in df.iterrows():
        base_prob = 0.12
        if row['Monthly_Income'] < 70000:
            base_prob += 0.15
        if row['Total_Working_Years'] < 3:
            base_prob += 0.10
        
        attrition_choice = np.random.choice(['Yes', 'No'], p=[min(base_prob, 0.85), 1 - min(base_prob, 0.85)])
        attrition_list.append(attrition_choice)
        
    # 3. Last me is naye column ko add kar dete hain taaki koi length ka error na aaye
    df['Attrition'] = attrition_list
    return df

if __name__ == "__main__":
    df = generate_hr_dataset()
    print(f"Successfully generated dataset with {df.shape} rows.")

