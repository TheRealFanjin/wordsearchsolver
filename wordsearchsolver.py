print('Type the letters here, pressing enter after each row. Press enter when done:')
listOfRows = []

# asks for row until nothing is entered
while True:
    a = input('>')
    if a == '':
        break
    listOfRows.append(a)

# separates listOfRows into separate letters
listOfLetters = [list(i) for i in listOfRows]


def checkHorizontal():
    indexPos = [None] * 2
    for counter, row in enumerate(listOfRows):
        try:
            try:
                indexPos[0] = counter
                indexPos[1] = row.index(word)
            except ValueError:
                indexPos[0] = counter
                indexPos[1] = row.index(word[::-1]) + (len(word) - 2)
        except ValueError:
            continue
    if all(indexPos):  # checks if indexPos has None in it
        print(indexPos)


def checkVertical():
    iterate = list(zip(*listOfLetters))
    verticalListOfLetters = []
    for item in iterate:
        verticalListOfLetters.append(''.join(item))
    indexPos = [None] * 2
    for counter, row in enumerate(verticalListOfLetters):
        try:
            try:
                indexPos[0] = row.index(word)
                indexPos[1] = counter
            except ValueError:
                indexPos[0] = row.index(word[::-1]) + (len(word) - 2)
                indexPos[1] = counter
        except ValueError:
            continue
    if all(indexPos):
        print(indexPos)





while True:
    word = input('Type the word you want to find: ')
    checkHorizontal()
    checkVertical()
