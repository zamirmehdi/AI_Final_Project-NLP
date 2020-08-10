file = open('/Users/apple/Desktop/Train_data.txt')
train_text = file.readlines()

file = open('/Users/apple/Desktop/Test_data.txt')
test_text = file.readlines()
file.close()

number_of_words = 0
unknown = '<UNK>'
none = '</s>'

unigram_counter = dict()
bigram_counter = dict()
trigram_counter = dict()

unigram_probability = dict()
bigram_probability = dict()
trigram_probability = dict()

unigram_counter[unknown] = 0


def unigram_counter_calculator():
    global unigram_counter
    global number_of_words
    for line in train_text:

        line.replace('"', '')
        line.replace(',', '')
        temp_words = line.split(' ')
        temp_words.remove(temp_words[len(temp_words) - 1])
        # temp_words[len(temp_words) - 1] = temp_words[len(temp_words) - 1].replace('.\n', '')
        # print('mmd', temp_words[len(temp_words) - 1], 'mmd')
        # break

        for word in temp_words:

            number_of_words += 1

            if unigram_counter.get(word) is None:
                unigram_counter[unknown] = unigram_counter.get(unknown) + 1
                unigram_counter[word] = 1

            else:
                unigram_counter[word] = unigram_counter.get(word) + 1

    print()

    print(unigram_counter.get('.\n'))
    print(number_of_words)
    print(len(unigram_counter))
    print(unigram_counter.get(unknown))
    print(sum(unigram_counter.values()))
    print(sum(unigram_counter.values()) - unigram_counter.get(unknown))
    print()


mmd = 0


def bigram_counter_calculator():
    global mmd
    global bigram_counter
    for line in train_text:

        line.replace('"', '')
        line.replace(',', '')
        temp_words = line.split(' ')
        temp_words.remove(temp_words[len(temp_words) - 1])

        for i in range(0, len(temp_words) + 1):

            last = ''

            if i == 0:
                current = temp_words[i]
                last = none
            elif i == len(temp_words):
                current = none
                last = temp_words[len(temp_words) - 1]
            else:
                current = temp_words[i]
                last = temp_words[i - 1]

            if bigram_counter.get((last, current)) is None:

                if bigram_counter.get((last, unknown)) is None:
                    bigram_counter[last, unknown] = 1
                else:
                    bigram_counter[last, unknown] = bigram_counter.get((last, unknown)) + 1
                    mmd += 1

                bigram_counter[last, current] = 1

            else:
                bigram_counter[last, current] = bigram_counter.get((last, current)) + 1
                mmd += 1

    print(bigram_counter.get(('the', 'U.S.')))
    print(len(bigram_counter))
    print(sum(bigram_counter.values()))
    print(mmd)
    print()


jas = 0


def trigram_counter_calculator():
    global trigram_counter
    global jas

    for line in train_text:

        line.replace('"', '')
        line.replace(', ', '')
        temp_words = line.split(' ')
        temp_words.remove(temp_words[len(temp_words) - 1])

        for i in range(0, (len(temp_words) + 1)):

            last = ''
            last_last = ''
            if len(temp_words) <= 1:
                continue
            if i == 0:
                current = temp_words[i]
                last = none
                last_last = none
            elif i == 1 and len(temp_words) > 1:
                current = temp_words[i]
                last = temp_words[i - 1]
                last_last = none
            elif i == len(temp_words):
                current = none
                last = temp_words[len(temp_words) - 1]
                last_last = temp_words[len(temp_words) - 2]
            else:
                current = temp_words[i]
                last = temp_words[i - 1]
                last_last = temp_words[i - 2]

            if trigram_counter.get((last_last, last, current)) is None:
                if trigram_counter.get((last_last, last, unknown)) is None:
                    trigram_counter[last_last, last, unknown] = 1
                    # if temp_words[48] == 'flu' and i == 1:
                    #     print('i:', i)
                    #     print(last_last, last, current)
                else:
                    trigram_counter[last_last, last, unknown] = trigram_counter.get((last_last, last, unknown)) + 1
                    jas += 1

                trigram_counter[last_last, last, current] = 1

            else:
                trigram_counter[last_last, last, current] = trigram_counter.get((last_last, last, current)) + 1
                jas += 1

    print(trigram_counter.get((none, 'The', 'U.S.')))
    print(len(trigram_counter))
    print((sum(trigram_counter.values())))
    print(jas)
    print()


def unigram_probability_calculator():
    global unigram_probability

    for elem in unigram_counter.keys():
        unigram_probability[elem] = unigram_counter.get(elem) / number_of_words


def bigram_probability_calculator():
    global bigram_probability

    for elem in bigram_counter.keys():
        total_amount = 0
        input_last = elem[0]
        input_current = elem[1]

        # bigram_probability[elem] = bigram_probability_calculator(elem[0], elem[1])
        if input_last != none:
            result = bigram_counter.get((input_last, input_current)) / unigram_counter.get(input_last)
        else:
            for key in bigram_counter.keys():
                if key[0] == none:
                    total_amount += bigram_counter.get(key)
            result = bigram_counter.get((input_last, input_current)) / total_amount

        bigram_probability[elem] = result


def trigram_probability_calculator():
    global trigram_probability

    for elem in trigram_counter.keys():
        total_amount = 0
        # trigram_probability[elem] = trigram_probability_calculator(elem[0], elem[1], elem[2])
        input_last_last = elem[0]
        input_last = elem[1]
        input_current = elem[2]

        if input_last != none:
            result = (trigram_counter.get((input_last_last, input_last, input_current))) / (bigram_counter.get((
                (input_last_last, input_last))))
        else:
            for key in trigram_counter.keys():
                if key[1] == none:
                    total_amount += trigram_counter.get(key)
            result = trigram_counter.get((input_last_last, input_last, input_current)) / total_amount

        trigram_probability[elem] = result


# def back_off(l1, l2, l3, ):



# print(unigram_probability_calculator('Abdullah'))
# print(unigram_counter.get('Abdullah'))


# for elem in unigram_counter.keys():
#     unigram_probability[elem] = unigram_probability_calculator(elem)

# print(len(bigram_counter))
# for elem in bigram_counter.keys():
#     bigram_probability[elem] = bigram_probability_calculator(elem[0], elem[1])

# for elem in trigram_counter.keys():
#     trigram_probability[elem] = trigram_probability_calculator(elem[0], elem[1], elem[2])
unigram_counter_calculator()
bigram_counter_calculator()
trigram_counter_calculator()
unigram_probability_calculator()
bigram_probability_calculator()
trigram_probability_calculator()

print(bigram_probability.get(('King', 'Abdullah')))
print()
print(len(trigram_probability))
print(len(trigram_counter))
print()

print(max(unigram_counter.values()))
print(list(unigram_counter.keys())[list(unigram_counter.values()).index(max(unigram_counter.values()))])

for line in test_text:

    # break
    temp_words = line.split(' ')

    if len(temp_words) < 2:
        continue

    temp_words.remove(temp_words[len(temp_words) - 1])

    temp_number = ''.join(filter(lambda x: x.isdigit(), temp_words[0]))
    temp_words[0] = ''.join(filter(lambda x: x.isalpha(), temp_words[0]))
    current_index = temp_words.index('$')

    # if current = 0

    break
