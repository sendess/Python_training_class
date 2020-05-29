import csv
import json


# sorted(iterable, keys)
with open('test_csv.csv','r') as f:
    content = list(csv.reader(f))
   # print(content)

    converted =[]
    keys = content[0]
    print(keys)

    for c in content[1:]:
        new = {}
        for key , val in zip(keys, c):
            new[key] = val
        converted.append(new)
    print(converted)


    sorted_csv = sorted(content[1:], key =lamda x: int(x[1]))

    for content in sorted_csv:
        print(content)