import datetime
from word_list import vocab_list

#just for testing purposes


def unjoin(db_word_list):
    word_items=db_word_list.split('*')
    new_list = [item.split('@') for item in word_items]
    second_list=[]
    for item in new_list:
        new_item=[]
        new_item.append(item[0].split('%'))
        new_item.append(datetime.datetime.strptime(item[1], "%Y-%m-%d %H:%M:%S"))
        new_item.append(datetime.timedelta(seconds=int(float(item[2]))))
        second_list.append(new_item)
    return second_list


def join_words(self):
        new_list =[]
        for item in self:
            new_item=[]
            new_item.append('%'.join(item[0]))
            new_item.append(item[1].strftime( "%Y-%m-%d %H:%M:%S"))
            new_item.append(str(item[2].total_seconds()))
            new_list.append('@'.join(new_item))
        return '*'.join(new_list)

def unjoin_dropped_words(string_of_words):
    word_items=string_of_words.split('@')
    return [item.split('%') for item in word_items]

def join_dropped_words(self):
        return '@'.join(['%'.join(word_info) for word_info in self])


new_ian_list=[[word, datetime.datetime.now().replace(microsecond=0), datetime.timedelta(seconds=17)] for word in vocab_list[:3]]
# # print(join_words(new_ian_list))
# print(unjoin(join_words(new_ian_list))[1])
# # print(vocab_list)
# print(new_ian_list[1])

# print(new_ian_list==unjoin(join_words(new_ian_list)))

print(join_dropped_words(vocab_list))
print(unjoin_dropped_words(join_dropped_words(vocab_list)))

