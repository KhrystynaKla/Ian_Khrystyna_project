import datetime


class User:
    def __init__(self, name):
        self.name=name
        self.words=[]
        self.dropped_words=[]

    def add_word(self, word):
        self.words.append([word, datetime.now(), timedelta(minutes=0)])

    def self_assess(self, word, level):
        for index, item in enumerate(self.words):
            if item[0]==word:
                if level==3 or item[2]== timedelta(minutes=0):
                    self.words[index] = [item[0], datetime.now(), timedelta(minutes=2)]
                elif level==2:
                    self.words[index] = [item[0], datetime.now(), timedelta(minutes=4)]
                else:
                    self.words[index] = [item[0], datetime.now(), 1.6*item[2]]



    def drop_word(self,word):
        self.dropped_words.append(word)
        print(self.dropped_words)

    
    

     

    