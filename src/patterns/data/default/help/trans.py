import csv

# Read the mapping from the first TSV file
def read_mapping(file_path):
    mapping = {}
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            if len(row) >= 2:
                mapping[row[1]] = row[0]
    return mapping

# Replace words in the second TSV file according to the mapping
def replace_words(mapping, input_file_path, output_file_path):
    with open(input_file_path, 'r', newline='', encoding='utf-8') as file:
        content = file.read()

    for target, replacement in mapping.items():
        content = content.replace(target, replacement)

    with open(output_file_path, 'w', newline='', encoding='utf-8') as file:
        file.write(content)

# File paths
mapping_file = 'labels.tsv'
input_file = 'radx-content-labels.tsv'
output_file = 'path_to_output_file.tsv'

# Execute the replacement
mapping = read_mapping(mapping_file)
replace_words(mapping, input_file, output_file)
