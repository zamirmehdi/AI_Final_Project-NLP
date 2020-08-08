file = open('/Users/apple/Desktop/Train_data.txt')

i = 0
for line in file:
    print(i + 1, ': ', line)
    i += 1
    if i > 19:
        break
