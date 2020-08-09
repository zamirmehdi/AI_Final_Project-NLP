file = open('/Users/apple/Desktop/Train_data.txt')
text = file.readlines()
number_of_words = 0

unknown = '<UNK>'
none = '</s>'

print(len(text))
print(text[2])

unigram_counter = dict()
bigram_counter = dict()
trigram_counter = dict()

unigram_counter[unknown] = 0
print(unigram_counter)

