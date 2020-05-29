import json
data = []
with open('data.json','r') as f:
    data = json.load(f)
print(data[0:2])
json_str = json.dumps(data[0])
print(json_str)
print(type(json_str))

temp = json.loads(json_str)
print(type(temp))

with open('second.json','w') as f:
    json.dump(temp, f)