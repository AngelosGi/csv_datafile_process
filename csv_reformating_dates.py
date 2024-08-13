import csv
import re
from datetime import datetime


input_file = 'data/processed_data/Greek_Parliament_Proceedings_1989_2020_DataSample_with_id.csv'
output_file = 'data/processed_data/Greek_Parliament_Proceedings_1989_2020_DataSample_with_id_and_formatted_date.csv'


def format_single_date(date_str):
    try:
        date_obj = datetime.strptime(date_str.strip(), '%d/%m/%Y')
        return date_obj.strftime('%Y-%m-%dT00:00:00Z')
    except ValueError:
        return date_str


def format_date_range(text):
    def replace_date_range(match):
        dates = match.group(1).split('-')
        if len(dates) == 2:
            formatted_dates = [format_single_date(d) for d in dates]
            return f"[{formatted_dates[0]} TO {formatted_dates[1]}]"
        elif len(dates) == 1:
            return format_single_date(dates[0])
        else:
            return match.group(0)  # Return original if not a valid date or range

    return re.sub(r'\(([\d/\-]+(?:-[\d/\-]+)?)\)', replace_date_range, text)


def format_value(value, is_sitting_date=False):
    if is_sitting_date:
        return format_single_date(value)

    # Check if the value is a list-like string
    if value.startswith('[') and value.endswith(']'):
        # Process each item in the list
        items = value[1:-1].split(',')
        formatted_items = [format_date_range(item.strip()) for item in items]
        return '[' + ', '.join(formatted_items) + ']'
    else:
        # If it's not a list, just format normally
        return format_date_range(value)


# Open the input file for reading and the output file for writing
with open(input_file, 'r', encoding='utf-8') as infile, \
        open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Read and write the header
    header = next(reader)
    writer.writerow(header)

    # Find the index of the 'sitting_date' column
    sitting_date_index = header.index('sitting_date')

    # Iterate through the rows, format all potential dates, and write to the new CSV
    for row in reader:
        formatted_row = [
            format_value(value, i == sitting_date_index)
            for i, value in enumerate(row)
        ]
        writer.writerow(formatted_row)

print(f"Created new CSV with all potential dates formatted: {output_file}")
