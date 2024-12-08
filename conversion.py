import json
import pandas as pd

# File path to the JSON file
json_file = 'filtered_articles.json'  # Replace with the actual path to your JSON file

# Read the JSON file
with open(json_file, 'r') as file:
    json_data = json.load(file)

# Convert JSON to DataFrame
df = pd.DataFrame(json_data)

df['publishedAt'] = pd.to_datetime(df['publishedAt']).dt.date


# Save DataFrame to Excel file
output_file = 'data2.xlsx'
df.to_excel(output_file, index=False, columns=['title', 'publishedAt', 'url'])

print(f"Data has been saved to {output_file}")
