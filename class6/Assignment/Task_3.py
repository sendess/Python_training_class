#       Task 3
#       Read the count.txt file and find the freq of every word and then write t
#       he word with frequency in a newcsv file with two columns, 
#       on with word and other with frequency


import csv
list_Title = ['Word','Frequency']
file_handler = open('count.txt', encoding="utf8")
count_text = str(file_handler.readlines())
#to remove unwanted symbols for word count
text = count_text.replace('.', '')
text = text.replace(',', '')
text = text.replace(';', '')
text = text.replace(':', '')
text = text.replace('?', '')
text = text.replace('-', '')
text = text.replace('/', '')
text = text.replace("\n", '')  #removing escape sequences
text = text.replace("\\n", '')  #removing escape sequences
text = text.replace("\\t", '')  #removing escape sequences
text = text.replace("\\s", '')  #removing escape sequences
text = text.replace("\\", '')
text = text.replace("'", '')
text = text.replace('"', '')
text = text.replace('(', '')
text = text.replace(')', '')
text = text.replace('[', '')
text = text.replace(']', '')
lower_text = (text.lower()).split()
file_handler.close
#which contains repeated words
#so creating set which removes repeated elements
non_repeat = set(lower_text)
file_handler = open('word_count.csv', 'w', newline='')
csv_writer = csv.writer(file_handler)
csv_writer.writerow(list_Title)
for i in non_repeat:
    data = (i, lower_text.count(i))
    csv_writer.writerow(data)
file_handler.close()