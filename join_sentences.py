


list_of_sentences = [['Today', 'is', 'a', 'good', 'day.'], \
                     ['Apples', 'are', 'my', 'favorite', 'fruit.']]

def join_sentence(list_of_sentences, index):
    sentence = " ".join(list_of_sentences[index])
    return sentence

sentence = join_sentence(list_of_sentences, 1)
print(sentence)
