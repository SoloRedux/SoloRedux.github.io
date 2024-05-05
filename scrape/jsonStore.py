import os
import json

def store(data):
    # Get the absolute path of the current file
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../scrap_data", "scrap.json")

    # Create the folder if it doesn't exist
    folder_path = os.path.dirname(file_path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Convert data to JSON format
    json_data = json.dumps(data, indent=4)

    # Store JSON data to the file
    with open(file_path, "w") as json_file:
        json_file.write(json_data)
        print("=====================================\n")
        print("Storing success at: \n(", file_path , ")")
        print("\n=====================================\n")
