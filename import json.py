import json

# Create a dictionary where the key and value are the same (1: 1, 2: 2, ..., 5000: 5000)
content_map = {str(i): i for i in range(1, 5001)}

# Save the content map to a JSON file
with open('content.json', 'w') as json_file:
    json.dump(content_map, json_file)

print("content.json file created with 5000 entries.")
