import time
import sys
sys.path.append('./packages')

from opcua import Client, ua

# Define the OPC UA server endpoint URL
url = "opc.tcp://192.168.1.2:4840/"

# Create a client object
client = Client(url)

# Set the username and password for authentication
username = "boschrexroth"
password = "boschrexroth"
client.set_user(username)
client.set_password(password)

# Track whether the connection was successful
connected = False

try:
    # Connect to the OPC UA server
    client.connect()
    print("Connected to OPC UA server.")
    connected = True  # Mark as connected

    # Get the root node
    root_node = client.get_root_node()

    # Get the objects node
    objects_node = root_node.get_child(["0:Objects"])

    # Define the namespace index and node paths
    namespace_index= 2
    node_path_toRead  = "system/health/memory-available/value"
    #node_path_toWrite = "plc/app/Application/sym/PLC_PRG/boolVar2"

    # Create a node ID for the variable
    #node_id_toWrite = ua.NodeId(node_path_toWrite, namespace_index)

    # Create a node ID for the variable
    node_id_toRead  = ua.NodeId(node_path_toRead , namespace_index )

    while True:
        # Read the value of the node
        try:
            variable_node = client.get_node(node_id_toRead )
            value = variable_node.get_value()
            print(f"Value of node '{node_path_toRead }': {value}")
        except ua.UaStatusCodeError as e:
            print(f"Error accessing node '{node_path_toRead }': {e}")


        # check node variable type if necessaty
        #node_to_write = client.get_node(node_id_toWrite)
        #data_type = node_to_write.get_data_type_as_variant_type()
        #print(f"Data type of node '{node_path_toWrite}' is {data_type}")

        # Read the value of the node
        #try:
        #    variable_node = client.get_node( node_to_write )
        #    value = variable_node.get_value()
        #    print(f"Value of node '{ node_to_write }': {value}")
        #except ua.UaStatusCodeError as e:
        #    print(f"Error accessing node '{ node_to_write }': {e}")

        # Set new value to differ from the last
        if value == True:
            new_value = False
        else:
            new_value = True
        
        # Write the value of the node
        #:
        #    variable_node.set_value(ua.Variant(new_value, ua.VariantType.Boolean))
        #    print(f"Successfully wrote {new_value} to node '{node_path_toWrite}'.")
        #except ua.UaStatusCodeError as e:
        #    print(f"Error writing to node '{node_path_toWrite}': {e}")

        # Wait before new cycle
        #time.sleep(1)

finally:
    # Disconnect from the OPC UA server if connected
    if connected:
        client.disconnect()
        print("Disconnected from OPC UA server.")
