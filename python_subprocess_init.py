import subprocess
subprocess.Popen(["gnome-terminal", "-e", "ionic serve"])
# Start the first program
process1 = subprocess.Popen(['python', 'python_json_update.py'])

# # Start the second program
process2 = subprocess.Popen(['python', 'python_firebase_data_update.py'])

# # Wait for both programs to finish
process1.wait()
process2.wait()



