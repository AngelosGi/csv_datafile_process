import pandas as pd

# Load the CSV data
csv_file_path = 'data/Greek_Parliament_Proceedings_1989_2020_DataSample.csv'
df = pd.read_csv(csv_file_path)

# Convert the DataFrame to JSON
json_data = df.to_json(orient='records', lines=True)

# Save the JSON data to a file
json_file_path = 'data/processed_data/p_Greek_Parliament_Proceedings_1989_2020_DataSample.json'
with open(json_file_path, 'w') as json_file:
    json_file.write(json_data)

print(f"JSON file created at: {json_file_path}")
