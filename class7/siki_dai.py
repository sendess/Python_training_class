import csv
data = []

with open('Monthly_Attendance.csv','r') as f:
    csv_reader = list(csv.reader(f,delimiter = ','))
    data = list(csv_reader)
    data.pop(0)

print(data[0])
temp = sorted(data, key= lambda x: int(x[7]), reverse = True)
for i in temp:
    print(i)

#with open('present.csv','w') as f:
