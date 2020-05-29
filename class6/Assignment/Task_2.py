#       Task 2
#       Convert the sample.csv file to sample.json file without using any external module

import csv
import json
with open ('sample.csv','r') as csv_file_handler:
    content = list(csv.reader(csv_file_handler))
    print(content)
    conv = []
    keys = content[0]
    print(keys)
    for c in content[1:]:
        new = {}
        for key, val in zip(keys,c):
            new[key] = val
        conv.append(new)
print(conv)
with open('sample_converted_to_json.json', 'w') as json_file_handler:
    json_file_handler.write(json.dumps(conv, indent = 4))# indent = 4 because    1 tab  = 4 spaces