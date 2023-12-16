import json

def read_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        
        return []
    except json.JSONDecodeError:
        
        return []

def write_data(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
    except FileNotFoundError:
        # Handle the case where the file is not found
        # You may create the file or log an error, depending on your use case
        pass
    except Exception as e:
        # Handle other exceptions (e.g., permission issues, etc.)
        # Log the error or perform appropriate error handling
        pass

