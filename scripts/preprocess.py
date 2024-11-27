import json

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def preprocess_data(data):
    # Add preprocessing steps like tokenization, filtering, etc.
    return data

if __name__ == "__main__":
    input_file = "data/training_data.json"
    output_file = "data/processed_data.json"

    raw_data = load_data(input_file)
    processed_data = preprocess_data(raw_data)

    with open(output_file, 'w') as file:
        json.dump(processed_data, file, indent=4)
    print("Data preprocessing complete!")
