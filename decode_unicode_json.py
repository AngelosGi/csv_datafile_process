import json

json_file_path = 'data/processed_data/p_Greek_Parliament_Proceedings_1989_2020_DataSample.json'

#Load the JSON data from the file
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    json_data = json_file.readlines()

#Decode Unicode escape sequences and print the data
decoded_data = [json.loads(record) for record in json_data]
for record in decoded_data[:5]:  # Print the first 5 records to check the structure
    print(record)
