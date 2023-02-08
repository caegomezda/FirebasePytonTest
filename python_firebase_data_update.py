import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time
import json
json_data = {}
def update_firestore_collection(docs, status_value):
    for doc in docs:
            doc_ref = doc.reference
            doc_ref.update({
                "status": status_value ,
            })
        # Wait for the specified time before updating again
        # time.sleep(sleep_time)

def import_json(file_path):
    # Load the JSON file
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data

def get_values(json_str, key):
    img_data_array=[]
    # Load the JSON data into a Python dictionary
    json_data = json_str["data"]
    # Check if the key is in the JSON data
    for data_img in json_data:
        if key in data_img:
            # Get the values for the key
            values = data_img[key]
            # Return the values as a list
            img_data_array.append(values)
        # Key is not in the JSON data
        else:
            return "Error empty json"
    return img_data_array

def array_distribution2update(collection_ref,img_data):

    for img in img_data:
        # Use the where() method to filter the documents you want to update
        query = collection_ref.where("name", "==", img[1])
        # Update the filtered documents
        docs = query.get()
        update_firestore_collection(docs,img)
    

if __name__ == '__main__':
     # Use a service account to access Firebase
    cred = credentials.Certificate(r'C:\Users\Edugoda\coding\Python\UparkingPython\uparkingpreview-firebase-adminsdk-uxlsw-33fb14f2db.json')
    firebase_admin.initialize_app(cred)
    # Connect to Firestore
    db = firestore.client()
    # Reference to the collection
    collection_ref = db.collection("imgMapParking")
    while True:
        json_data = import_json(r'C:\Users\Edugoda\coding\Python\UparkingPython\python_json_data.json')
        img_data_array = get_values(json_data,"status")
        array_distribution2update(collection_ref,img_data_array)
        time.sleep(10)



