import json
import re


def convert_to_json(file_path, output_path):
    data = []

    # Read the file and process each line
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Split the line by '|'
            columns = line.strip().split('|')
            # Extract the necessary columns (remove the traditional Chinese column)
            simplified = columns[2]  # Simplified Chinese
            pinyin = columns[3]      # Pinyin
            meaning = columns[4]     # Meaning
            # Remove any audio references enclosed in {{}} from the meaning
            meaning_cleaned = re.sub(r'\{\{.*?\}\}', '', meaning).strip()
            # Create a dictionary for each entry
            entry = {
                "Simplified": simplified,
                "Pinyin": pinyin,
                "Meaning": meaning_cleaned
            }
            data.append(entry)

        with open(output_path, "a") as mandarin:
            json.dump(data, mandarin, indent=4)

        print(meaning_cleaned)
    # Save the data to a JSON file


# Usage example
file_path = 'data.txt'  # Replace with the path to your text file
output_path = 'mandarin.json'  # Replace with your desired output path
convert_to_json(file_path, output_path)
