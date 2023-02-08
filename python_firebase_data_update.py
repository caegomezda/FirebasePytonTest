from tkinter import FALSE
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time

# Use a service account to access Firebase
# cred = credentials.Certificate('C:\Users\Edugoda\coding\Python\UparkingPython\uparkingpreview-firebase-adminsdk-uxlsw-33fb14f2db.json')
cred = credentials.Certificate(r'C:\Users\Edugoda\coding\Python\UparkingPython\uparkingpreview-firebase-adminsdk-uxlsw-33fb14f2db.json')

firebase_admin.initialize_app(cred)

# Connect to Firestore
db = firestore.client()

# Reference to the collection
collection_ref = db.collection(u'imgMapParking')
n = 0
while True:
    # Use the where() method to filter the documents you want to update
    query = collection_ref.where("name", "==", "img_1")

    # Update the filtered documents
    docs = query.get()
    n = n + 1
    for doc in docs:
            doc_ref = doc.reference
            doc_ref.update({
                "status": n ,
                # "field_2_to_update": new_value_2,
                # ...
            })

    # Wait for one minute before updating again
    time.sleep(10)
#C:\Users\Edugoda\AppData\Local\Programs\Python\Python311


# Reference the collection you want to update
collection_ref = db.collection("collection_name")


