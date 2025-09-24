from flask import Flask, jsonify
import ctrlXapi as ctX
import time
import threading

app = Flask(__name__)

# ctrlX parameters
address = "192.168.1.1"
user = "boschrexroth"
password = "boschrexroth"

# Datalayer paths
vGroup = "plc/app/Application/sym/my_GVLs/"
vBool = "booleanToAPI"
vString = "stringToAPI"

data_values = {}

def cyclic_read_write():
    global data_values
    try:
        token = ctX.get_token(address, user, password)
        while True:
            # Read values
            bool_value = ctX.get_value(address, token, vGroup + vBool)
            string_value = ctX.get_value(address, token, vGroup + vString)
            
            # Store values
            data_values[vBool] = bool_value
            data_values[vString] = string_value
            
            # Toggle boolean value
            new_bool_value = not bool_value if isinstance(bool_value, bool) else True
            ctX.set_value(address, token, vGroup + vBool, "bool8", new_bool_value)
            
            # Update string value
            ctX.set_value(address, token, vGroup + vString, "string", "Updated by Flask API")
            
            time.sleep(5)  # Adjust cycle time as needed
    except Exception as e:
        print("Error in cyclic operation:", e)

# Start cyclic process in a separate thread
threading.Thread(target=cyclic_read_write, daemon=True).start()

@app.route('/', methods=['GET'])
def get_data():
    return jsonify(data_values)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)