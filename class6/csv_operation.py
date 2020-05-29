import csv

subject = ['name','python', 'data structure', 'physics']

#with open('marksheet.csv','w') as f:
 #   csv_writer = csv.writer(f)
 #   csv_writer.writerow(subject)

marks = [
    ['john', 12, 34, 53],
    ['Rohit', 23, 42,34],
    ['angel', 22, 42, 36]
]
with open('marksheet.csv','r+') as f:
    csv_writer = csv.writer(f, delimiter = ':')
    csv_writer.writerow(subject)
    csv_writer.writerows(marks)


with open('marksheet.csv','r') as f:
    csv_reader = csv.reader(f,delimiter = ':')
    for i in csv_reader:
        print(i)


#comment below codes if markshee empty
with open('marksheet.csv','w') as f:
    csv_writer = csv.DictWriter(f, delimiter = ',', fieldnames=['name','maths'])
    dat = {
        'name':'john',
        'math' : 40
    }