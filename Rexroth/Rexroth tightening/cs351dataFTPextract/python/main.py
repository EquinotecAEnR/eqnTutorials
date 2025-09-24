from ftplib import FTP
import base64
import json
from io import BytesIO

# --- FTP Connection Details ---
FTP_HOST = "192.168.1.1"
FTP_PORT = 21
FTP_USER = "imsoft"
FTP_PASS = "Robert"
FILE_NAME = "data_base64.txt"  # Change to the file name you expect

# --- Connect to FTP and Download File ---
ftp = FTP()
ftp.connect(FTP_HOST, FTP_PORT)
ftp.login(FTP_USER, FTP_PASS)

# Use BytesIO to avoid saving file locally
file_data = BytesIO()
ftp.retrbinary(f"RETR {FILE_NAME}", file_data.write)
ftp.quit()

# --- Decode Base64 ---
file_data.seek(0)
base64_string = file_data.read().decode('utf-8').strip()

try:
    json_bytes = base64.b64decode(base64_string)
    json_str = json_bytes.decode('utf-8')
    data = json.loads(json_str)
except Exception as e:
    print("Error decoding or parsing data:", e)
    exit(1)

# --- Extract Fields ---
node_id = data.get("node id")
result = data.get("result")
hardware = data.get("hardware")
mce_list = data.get("MCE", [])

mce_functions = [{
    "function": m.get("Transducer function"),
    "measuring": m.get("measuring"),
    "partNumber": m.get("part number")
} for m in mce_list]

# --- Print Results ---
print(f"Node ID: {node_id}")
print(f"Result: {result}")
print(f"Hardware: {hardware}")
print("MCE Functions:")
for i, mce in enumerate(mce_functions, 1):
    print(f"  {i}. Function: {mce['function']}, Measuring: {mce['measuring']}, Part #: {mce['partNumber']}")
