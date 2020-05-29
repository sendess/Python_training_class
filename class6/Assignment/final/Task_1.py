#       Task 1
#       Sort the Monthly_Attendance.csv in descending order according to attendance number then find the  \
#       top 100 students with largest attendace and write the sorted information in a new present.csv file
import csv
data = []
line = 0
top_100 = []
c = 0
f = open('Monthly_Attendance.csv','r')
fp = open('100_sorted.csv', 'w', newline='') #newline= '' used as windows by default moves the writing cursor to new line on write mode
csv_reader = list(csv.reader(f, delimiter = ','))
data = list(csv_reader)
print(":::::::::::::::::::::::::::::::::::::::Attendance record in decending order of present students::::::::::::::::::::::::::::::::::::::;:")
for i in data:
    print(i)
    top_100.append(i)
    c += 1
    if c == 1:
        break
data.pop(0)
csv_writer = csv.writer(fp, delimiter = ',')
temp = sorted(data, key= lambda x: int(x[7]), reverse = True)
for i in temp:
    print(i)
for i in temp:
    top_100.append(i)
    line += 1
    if line == 100:
        break
print("----------------------Top 100 data have been exported to file 100_sorted.csv!!!!!!")
csv_writer.writerows(top_100)
f.close()
fp.close()  
