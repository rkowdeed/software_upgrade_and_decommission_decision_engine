import pandas as pd
from datetime import datetime

# Sample CSV data

# Create a DataFrame from the CSV data
df = pd.read_csv("csv_data.txt")
print(df)

# Function to generate recommendations
def generate_recommendations(df):
    recommendations = []

    current_date = datetime.now()

    for index, row in df.iterrows():
        software_name = row['Software Name']
        version = row['Version']
        eol_date = datetime.strptime(row['End of Life Date'], '%Y-%m-%d')
        usage = row['Current Usage']
        risk_level = row['Risk Level']

        if eol_date < current_date:
            action = 'Decommission'
        elif risk_level == 'High' or usage == 'High':
            action = 'Upgrade'
        else:
            action = 'Monitor'

        recommendations.append({
            'Software Name': software_name,
            'Current Version': version,
            'Recommended Action': action
        })

    return recommendations

# Generate recommendations
recommendations = generate_recommendations(df)

# Output the recommendations
for recommendation in recommendations:
    print(f"Software: {recommendation['Software Name']}, "
          f"Version: {recommendation['Current Version']}, "
          f"Action: {recommendation['Recommended Action']}")
