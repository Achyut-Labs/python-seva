import yaml
import base64
import json
import re

def find_control_chars(s):
    return [i for i, c in enumerate(s) if ord(c) < 32 and c != '\n' and c != '\r' and c != '\t']

# Load the YAML file
with open('your_file.yaml', 'r') as file:
    yaml_content = yaml.safe_load(file)

# Extract the base64-encoded JSON (adjust the path as needed)
base64_json = yaml_content['path']['to']['base64']['encoded']['json']

# Decode the base64 content
decoded_json = base64.b64decode(base64_json).decode('utf-8')

# Find control characters
control_char_positions = find_control_chars(decoded_json)

if control_char_positions:
    print(f"Control characters found at positions: {control_char_positions}")
    for pos in control_char_positions:
        print(f"Character at position {pos}: {repr(decoded_json[pos])}")
else:
    print("No control characters found.")

# Optionally, try to parse the JSON to check for validity
try:
    json.loads(decoded_json)
    print("JSON is valid.")
except json.JSONDecodeError as e:
    print(f"JSON is invalid: {str(e)}")
