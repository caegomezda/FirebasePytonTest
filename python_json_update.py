import json
import time
import random

def import_json(file_path):
    # Load the JSON file
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data

def update_json(json_str, key, new_value):
    # Load the JSON data into a Python dictionary
    json_data = json.loads(json_str)

    # Check if the key is in the JSON data
    if key in json_data:
        # Update the value for the key
        json_data[key] = new_value

        # Convert the dictionary back to a JSON string
        updated_json = json.dumps(json_data)

        return updated_json

    # Key is not in the JSON data
    else:
        return json_str

def update_json_random(json_str, updates):
    # json_data = json_str["data"]
    # Loop through the updates dictionary
    print("________________________________")
    print("original")
    print(json_str)
    print("*******************************")

    for item in json_str["data"]:
        new_value = random.choice(updates)
        # Check if the key is in the JSON data
        # Get a random value from the values list
        # Update the value for the key
        item["status"][0] = new_value

    # Convert the dictionary back to a JSON string
    # updated_json = json.dumps(json_data)
    updated_json = json_data

    print("________________________________")
    print("update")
    print(updated_json)
    print("*******************************")
    with open('python_json_data.json', 'w') as file:
        # Write the updated JSON data back to the file
        json.dump(updated_json, file)
    # return updated_json



if __name__ == '__main__':
    while True:
        json_data = import_json(r'C:\Users\Edugoda\coding\Python\UparkingPython\python_json_data.json')
        json_update = ["FULL","EMPTY"]
        update_json_random(json_data,json_update)
        time.sleep(5)