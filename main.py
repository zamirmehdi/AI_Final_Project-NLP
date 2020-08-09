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

for line in text:

    temp_words = line.split(' ')

    for word in temp_words:

        number_of_words += 1

        if unigram_counter.get(word) is None:
            unigram_counter[unknown] = unigram_counter.get(unknown) + 1
            unigram_counter[word] = 0
        # if not any(word == unigram_words for unigram_words in unigram_probability.keys()):

        else:
            unigram_counter[word] = unigram_counter.get(word) + 1

print(unigram_counter.get('.\n'))
print(number_of_words)
print(sum(unigram_counter.values()))

