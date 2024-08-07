import csv

# Input and output file names
input_file = 'data/Greek_Parliament_Proceedings_1989_2020_DataSample.csv'
output_file = 'data/processed_data/Greek_Parliament_Proceedings_1989_2020_DataSample_with_id.csv'

# Open the input file for reading and the output file for writing
with open(input_file, 'r', encoding='utf-8') as infile, \
        open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    # Create CSV reader and writer objects
    reader = csv.reader(infile)

    # Read the header
    header = next(reader)

    # Add 'id' to the beginning of the header
    new_header = ['id'] + header

    writer = csv.writer(outfile)

    # Write the new header to the output file
    writer.writerow(new_header)

    # Iterate through the rows, add an ID, and write to the new CSV
    for i, row in enumerate(reader, 1):
        new_row = [f'speech_{i}'] + row
        writer.writerow(new_row)

print(f"Created new CSV with IDs: {output_file}")
