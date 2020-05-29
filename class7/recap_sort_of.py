'''
load
loads
dump
dumps

'''
import json

with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)


print(data[0]['userId'])
print(type(data[0]))


dict_str = '{"name": "test","age": 12}'
print(type(dict_str))

dict_obj = json.loads(dict_str)
print(type(dict_obj))

#dump and dumps

with open('try.json','w')as f:
    json.dump(dict_obj, f)

dict_str = {"name": "test","age": 12}
dict_s = json.dumps(dict_str)
print(type(dict_s))

#CSV aba


import csv

subject = {'name', 'python', 'data_structure','c++'}
with open('marksheet.csv','w') as f:
    csv_wrtiter = csv.writer(f,delimiter = ',')
    csv_wrtiter.writerow(subject)

marks = [
    ['jhon', 12, 23, 42],
    ['dasd', 12, 23, 42],
    ['123', 12, 23, 42],
]

with open('marksheet.csv', 'a') as f:
    csv_writer = csv.writer(f,delimiter = ',')
    csv_writer.writerows(marks)

with open('marksheet.csv', 'r') as f:
    csv_reader = list(csv.reader(f, delimiter = ':'))
    for i in csv_reader:
        print(i)

with open('marksheet.csv','r+')as f:
    f.read()
    print(f.tell())
    csv_writer = csv.writer(f , delimiter = "-")

    