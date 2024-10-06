import csv

# Function to convert CSV data to JavaScript array format
def convert_csv_to_js_array(csv_filename):
    quotes = []
    
    # Read the CSV file
    with open(csv_filename, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            # Format each quote with author and add to the list
            quotes.append(f'"{row["Quote"]} {row["Author"]}"')
    
    # Create the final JavaScript constant declaration

    js_array = "const quotes = [\n    " + ",\n    ".join(quotes) + "\n];"
    
    return js_array

# Specify your CSV file name
csv_file = 'quotes.csv'
js_output = convert_csv_to_js_array(csv_file)
# Specify the output file name
output_file = 'quote.js'

# Write the output to a file
with open(output_file, mode='w', encoding='utf-8') as f:
    f.write(js_output)

