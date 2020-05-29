#       Task 3
#       Write a class with that has an attribute which stores a multi word string,
#       and a method that gives that string in reverse order word-by-word


class Statement:
    string_list = None
    sentence = None

    def __init__(self, sentence):
        self.sentence = sentence.replace(',' , '')
        self.sentence = sentence.replace('.' , '')
        self.string_list = self.sentence.split()
        self.string_list = self.string_list[::-1]

    def display_reverse(self):
        string_reverse = ""  
        # traverse in the string   
        for i in self.string_list:  
            string_reverse += i
            string_reverse += ' '
        print(string_reverse)
        
string_hold_1 = str(input("Enter a sentence to be reversed : \n"))
object_string_1 = Statement(string_hold_1)
object_string_1.display_reverse()
