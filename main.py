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
# bigram_counter[none, unknown] = 0
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

mmd = 0
for line in text:

    temp_words = line.split(' ')

    for i in range(0, len(temp_words)):

        mmd += 1
        last = ''
        if i == 0:
            last = none
        else:
            last = temp_words[i - 1]
        # if i == 0:
        #     if bigram_counter.get((none, temp_words[i])) is None:
        #         bigram_counter[none, unknown] = bigram_counter.get((none, unknown)) + 1
        #         bigram_counter[none, temp_words[i]] = 0
        #     else:
        #         bigram_counter[none, temp_words[i]] = bigram_counter.get((none, temp_words[i])) + 1

        # elif i == len(temp_words) - 1:
        # if bigram_counter.get((temp_words[i], none)) is None:
        #     bigram_counter[unknown, none] = bigram_counter.get((unknown, none)) + 1
        #     bigram_counter[temp_words[i], none] = 0
        # else:
        #     bigram_counter[temp_words[i], none] = bigram_counter.get((temp_words[i], none)) + 1

        # else:
        if bigram_counter.get((last, temp_words[i])) is None:
            if bigram_counter.get((last, unknown)) is None:
                bigram_counter[last, unknown] = 0
            else:
                bigram_counter[last, unknown] = bigram_counter.get((last, unknown)) + 1

            bigram_counter[last, temp_words[i]] = 0

        else:
            bigram_counter[last, temp_words[i]] = bigram_counter.get((last, temp_words[i])) + 1

print(bigram_counter.get(('the', 'U.S.')))
print(sum(bigram_counter.values()))
print(mmd)
