class Sentence:
    word_list = None
    sentence = None

    def __init__(self, sentence):
        self.sentence = sentence.lower().replace(',' or ',', '')
        self.word_list = self.sentence.split()
        self.word_list = self.word_list[::-1]

    def display_rev_list(self):
        print(self.word_list)


sc1 = Sentence('This is a sentence which is to be displayed in reverse order.')
sc1.display_rev_list()
