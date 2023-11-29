import datetime
from __init__ import CONN, CURSOR
from word_list import vocab_list

def unjoin(db_word_list):
    word_items=db_word_list.split('*')
    new_list = [item.split('@') for item in word_items]
    second_list=[]
    if new_list==[['']]:
        new_list=[]
    for item in new_list:
        new_item=[]
        new_item.append(item[0].split('%'))
        new_item.append(datetime.datetime.strptime(item[1], "%Y-%m-%d %H:%M:%S"))
        
        new_item.append(datetime.timedelta(seconds=int(float(item[2]))))
        second_list.append(new_item)
    return second_list

def unjoin_dropped_words(string_of_words):
    word_items=string_of_words.split('@')
    return [item.split('%') for item in word_items]



class User:
    def __init__(self, name, words=[], dropped_words=[], id= None):
        self.id=id
        self.name=name
        self.words=words
        self.dropped_words=dropped_words

    def add_word(self, word):
        self.words.append([word, datetime.datetime.now().replace(microsecond=0), datetime.timedelta(minutes=1)])
        sql = '''UPDATE users SET words = ?
        WHERE id = ?
        '''
        CURSOR.execute(sql, [self.join_words(), self.id])
        #GIT ADD
        CONN.commit()
        # updates the row based on current attributes 

    def self_assess(self, word, level):
        for index, item in enumerate(self.words):
            if item[0]==word:
                if level==3 or item[2]== datetime.timedelta(minutes=1):
                    self.words[index] = [item[0], datetime.datetime.now(), datetime.timedelta(minutes=2)]
                elif level==2:
                    self.words[index] = [item[0], datetime.datetime.now(), datetime.timedelta(minutes=4)]
                else:
                    self.words[index] = [item[0], datetime.datetime.now(), 1.6*item[2]]
        sql = '''UPDATE users SET words = ?
        WHERE id = ?
        '''
        CURSOR.execute(sql, [self.join_words(), self.id])
        #GIT ADD
        CONN.commit()
        # updates the row based on current attributes 

    def drop_word(self,word):
        self.dropped_words.append(word)
        sql = '''UPDATE users SET dropped_words = ?
        WHERE id = ?
        '''
        CURSOR.execute(sql, [self.join_dropped_words(), self.id])
        #GIT ADD
        CONN.commit()
        # updates the row based on current attributes 


    def join_words(self):
        new_list =[]
        sorted_list_of_words=sorted(self.words, key=lambda word : word[1]+word[2])
        for item in sorted_list_of_words:
            new_item=[]
            new_item.append('%'.join(item[0]))
            new_item.append(item[1].strftime( "%Y-%m-%d %H:%M:%S"))
            new_item.append(str(item[2].total_seconds()))
            new_list.append('@'.join(new_item))
        return '*'.join(new_list)
    
    def join_dropped_words(self):
        return '@'.join(['%'.join(word_info) for word_info in self.dropped_words])

    def create(self):
        sql ='''INSERT INTO users (name, words, dropped_words)
        VALUES (?,?,?)
        '''
        CURSOR.execute(sql, [self.name, self.join_words(), self.join_dropped_words()])
        #GIT ADD
        CONN.commit()
        #GIT COMMIT
        # creates in the db and updates instance with the new id
        last_row_sql = 'SELECT * FROM users ORDER BY id DESC LIMIT 1'
        last_row_tuple = CURSOR.execute(last_row_sql).fetchone()
        self.id=last_row_tuple[0]

    @classmethod
    def get_all_users(cls):
        sql='''SELECT * fROM users
        '''
        read_all_tuples=CURSOR.execute(sql).fetchall()
        all_users =[]
        for tup in read_all_tuples:
            all_users.append(User(name=tup[1], id=tup[0], words=unjoin(tup[2]), dropped_words=unjoin_dropped_words(tup[3])))
        return all_users
    
    def timeless_words(self):
        return [word[0] for word in self.words]

    
    def list_of_words_to_review(self):
        words_due=[word[0] for word in self.words if word[1]+word[2]<datetime.datetime.now() and word[0] not in self.dropped_words]
        if len(words_due)>=20:
            return words_due[:20]
        else:
            current_list=words_due
            for curr_word in vocab_list:
                if len(current_list)==20:
                    return current_list
                else:
                    if curr_word not in self.timeless_words():
                        current_list.append(curr_word)
            return current_list
    
    


    

     

    