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

        else:
            unigram_counter[word] = unigram_counter.get(word) + 1

print(unigram_counter.get('.\n'))
print(number_of_words)
print(sum(unigram_counter.values()))
print()

mmd = 0
for line in text:

    temp_words = line.split(' ')

    for i in range(0, len(temp_words)):

        current = temp_words[i]
        last = ''

        if i == 0:
            last = none
        else:
            last = temp_words[i - 1]

        if bigram_counter.get((last, current)) is None:

            if bigram_counter.get((last, unknown)) is None:
                bigram_counter[last, unknown] = 0
            else:
                bigram_counter[last, unknown] = bigram_counter.get((last, unknown)) + 1
                mmd += 1

            bigram_counter[last, current] = 0

        else:
            bigram_counter[last, current] = bigram_counter.get((last, current)) + 1
            mmd += 1

print(bigram_counter.get(('the', 'U.S.')))
print(len(bigram_counter))
print(sum(bigram_counter.values()))
print(mmd)
print()

jas = 0
for line in text:

    temp_words = line.split(' ')
    for i in range(0, len(temp_words)):

        current = temp_words[i]
        last = ''
        last_last = ''

        if i == 0:
            last = none
            last_last = none
        elif i == 1:
            last = temp_words[i - 1]
            last_last = none
        else:
            last = temp_words[i - 1]
            last_last = temp_words[i - 2]

        if trigram_counter.get((last_last, last, current)) is None:
            if trigram_counter.get((last_last, last, unknown)) is None:
                trigram_counter[last_last, last, unknown] = 0
            else:
                trigram_counter[last_last, last, unknown] = trigram_counter.get((last_last, last, unknown)) + 1
                jas += 1

            trigram_counter[last_last, last, current] = 0

        else:
            trigram_counter[last_last, last, current] = trigram_counter.get((last_last, last, temp_words[i])) + 1
            jas += 1

print(trigram_counter.get((none, 'The', 'U.S.')))
print(len(trigram_counter))
print((sum(trigram_counter.values())))
print(jas)
