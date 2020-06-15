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
                indexPos[0] = counter + 1
                indexPos[1] = row.index(word) + 1
                print("'" + word + "'", 'found at', indexPos, 'going right')
            except ValueError:
                indexPos[0] = counter + 1
                indexPos[1] = row.index(word[::-1]) + (len(word)) + 1
                print("'" + word + "'", 'found at', indexPos, 'going left')
        except ValueError:
            continue


def checkVertical():
    iterate = list(zip(*listOfLetters))
    verticalListOfLetters = [''.join(item) for item in iterate]
    indexPos = [None] * 2
    for counter, row in enumerate(verticalListOfLetters):
        try:
            try:
                indexPos[0] = row.index(word) + 1
                indexPos[1] = counter + 1
                print("'" + word + "'", 'found at', indexPos, 'going down')
            except ValueError:
                indexPos[0] = row.index(word[::-1]) + (len(word)) + 1
                indexPos[1] = counter + 1
                print("'" + word + "'", 'found at', indexPos, 'going up')
        except ValueError:
            continue


while True:
    word = input('Type the word you want to find: ')
    checkHorizontal()
    checkVertical()

