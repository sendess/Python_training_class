#       Task 3 
#       Read the count.txt file and find the freq of every word and then write the word \
#       with frequency in a new csv file with two columns, on with word and other with frequency
import csv
list_dict = []
list_freq = []
file_handler = open('count.txt', encoding="utf8")
count_text = str(file_handler.readlines())
text = count_text.replace('.', '')
text = text.replace(',', '')
text = text.replace(';', '')
text = text.replace(':', '')
text = text.replace('?', '')
text = text.replace('-', '')
text = text.replace('/', '')
text = text.replace('\n', '')
text = text.replace("'", '')
text = text.replace('"', '')
text = text.replace('(', '')
text = text.replace(')', '')
text = text.replace('[', '')
text = text.replace(']', '')
lower_text = (text.lower()).split()
file_handler.close


file_handler.close
def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

dict_for_count = word_count(lower_text)
print(dict_for_count)

for i,j in dict_for_count.items():
    list_dict.append ((i,j))
print (list_dict)

title =['Word', 'Frequency']
list_freq.append(title)
list_freq.append(list_dict)
print(list_freq)
file_handler = open('word_count.csv','w')
csv_writer = csv.writer(file_handler, delimiter = ',')
csv_writer.writerows(list_freq)
file_handler.close()

    