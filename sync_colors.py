import json

multiple_path = '/Users/scm2mjc/Desktop/Code/wales-senedd-2026/data/senedd_2026_multiple.hexjson'
nc_path = '/Users/scm2mjc/Desktop/Code/wales-senedd-2026/data/senedd_2026_nc.hexjson'

with open(multiple_path, 'r') as f:
    multiple_data = json.load(f)

with open(nc_path, 'r') as f:
    nc_data = json.load(f)

# Extract mapping English_Na -> colour from multiple_data
color_mapping = {}
for hex_id, hex_data in multiple_data['hexes'].items():
    if 'English_Na' in hex_data and 'colour' in hex_data:
        color_mapping[hex_data['English_Na']] = hex_data['colour']

# Apply mapping to nc_data
for hex_id, hex_data in nc_data['hexes'].items():
    eng_name = hex_data.get('English_Na')
    if eng_name in color_mapping:
        hex_data['colour'] = color_mapping[eng_name]

with open(nc_path, 'w') as f:
    json.dump(nc_data, f, indent=4)

print(f"Successfully updated {nc_path} with colors from {multiple_path}")
