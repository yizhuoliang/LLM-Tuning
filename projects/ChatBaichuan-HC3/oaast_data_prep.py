import json

def transform_dataset(input_file, output_file):
    # Open the input file and load the JSON data
    with open(input_file, 'r') as infile:
        data = json.load(infile)

    # Initialize the output data
    output_data = []

    # Process each entry in the input data
    for entry in data:
        # Extract the 'instruction' and 'history' fields
        instruction = entry['instruction']
        history = entry['history']

        # Combine the history and instruction into a single string,
        # separated by newlines. Here we use nested loops to handle
        # the case where 'history' is a list of lists of strings.
        q = ""
        coin = 0
        for sublist in history:
            for item in sublist:
                if coin == 0:
                    q += "q:" + item + "\n"
                    coin = 1
                else:
                    q += "a:" + item + "\n"
                    coin = 0
        q += instruction

        # Copy the 'output' field
        a = entry['output']

        # Create a new dictionary with 'q' and 'a' fields,
        # and add it to the output data
        output_data.append({'q': q, 'a': a})
    print(len(output_data))

    # Open the output file and write the output data to it
    # 'ensure_ascii=False' makes the json.dump not escape non-ASCII characters
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for entry in output_data:
            json_str = json.dumps(entry, ensure_ascii=False)
            outfile.write(json_str + "\n")

# Invoke the function with the names of the input and output files
transform_dataset('oaast_sft_zh.json', 'output.json')