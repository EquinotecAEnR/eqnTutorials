# Import ctrlXapi methods
import ctrlXapi as ctX


# ctrlX parameters:
address="192.168.1.1"
user="boschrexroth"
password="boschrexroth"

# Datalayer pathts
## Group of Variables
vGroup="plc/app/Application/sym/my_GVLs/"

## Variables to read/write:
vBool="booleanToAPI"
vString="stringToAPI"


# Main execution
if __name__ == "__main__":
    try:
        # Get Token from authentication
        token = ctX.get_token(address, user, password)
        print(token)
        input("\n Got token from authentication \n Press Enter to continue...\n")

        ## Use Boolean ##
        # Get Single Boolean
        print(ctX.get_value(address,token, (vGroup+vBool)))
        input(f"\n got variable '{vBool}' value \n Press Enter to continue... \n")

        # Set Single Boolean
        print(ctX.set_value(address,token, (vGroup+vBool),"bool8", True))
        input(f"\n {vBool} value was writen to 'TRUE' \n Press Enter to continue... \n")


        ## Use String ##
        # get Single String
        print(ctX.get_value(address,token, (vGroup+vString)))
        input(f"\n got variable'{vString}' value \n Press Enter to continue... \n")

        # Set Single String
        print(ctX.set_value(address,token, (vGroup+vString),"string", "this was a test"))
        input(f"\n {vString} value was writen to 'this was a test' \n Press Enter to continue... \n")

        # Browse for available values
        available_data=ctX.browse_data(address,token, vGroup)

        print(available_data)
        input("\n Got available data browsed: \n Press Enter to continue...\n")

        # Use browsed data names to get values
        data_values = {}
        for data in available_data.get('value', []):
            data_value = ctX.get_value(address,token, vGroup+data)
            data_values[data] = data_value
        print(f"Value for {data}:", ctX.json.dumps(data_values, indent=4))
        input(f"\n got all browsed values from {vGroup} \n Press Enter to continue...\n")

        # Reset Values
        print(ctX.set_value(address,token, (vGroup+vBool),"bool8", False))
        print(ctX.set_value(address,token, (vGroup+vString),"string", "this is a test"))
        
        input("\n Values were reseted \n Press Enter to end example.")

 

    except ctX.requests.exceptions.RequestException as e:
        print("HTTP Request failed:", e)
    except ValueError as e:
        print("Error:", e)
