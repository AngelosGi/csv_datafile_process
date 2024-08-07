# CSV datafile process

## Description
The `csv_to_json_converter` script is a simple and efficient Python tool designed to edit a CSV file, specifically the `Greek_Parliament_Proceedings_1989_2020_DataSample.csv`, 
Add id to the rows
convert it to a JSON file. It reads the input CSV file, processes the data, and outputs the data in JSON format, making it easier to work with in various applications and workflows. (My use case: Elasticsearch and Apache Solr)
## Features
- Adds id to the CSV rows
- Converts a CSV file to JSON format.
- Decode the Unicode escape sequences, and print the first five records in a human-readable format (for testing) (for when we convert it to JSON)
- Easy to use with minimal configuration required.

