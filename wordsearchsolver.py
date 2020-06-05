print('Type the letters here, pressing enter after each row. Press enter when done:')
listOfLetters = []
indexPos = []
i = 0
while True:
    a = input()
    if a == '':
        break
    listOfLetters.append(a)
    print(listOfLetters)
    i +=1
def checkHorizontal():
    indexPos = [None]*2
    for counter, row in enumerate(listOfLetters):
        try:
            try:
                indexPos[0] = row.index(word)
                indexPos[1] = counter
            except ValueError:
                indexPos[0] = row.index(word[::-1])
                indexPos[1] = counter
        except ValueError:
            continue
    return indexPos

while True:
    word = input('Type the word you want to find: ')
    print(checkHorizontal())