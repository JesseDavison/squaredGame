import random





def bombNumber(num, bombSize):
    entities = []
    for x in range(bombSize):
        chunkSize = int(num / bombSize)
        entities.append(chunkSize)
        remainder = num % bombSize
    # print(str(num) + " and " + str(bombSize) + "bomb")
    # print(str(num) + " with a " + str(bombSize) + "bomb gives us: " + str(bombSize) + " chunks of size " + str(chunkSize) + " and remainder of " + str(remainder))
    # print("entities: " + str(entities) + "    trash:" + str(remainder))
    # e.g, split 16 with a "bomb" of size 4 results in: 4 new entities of 4 each
    # e.g. split 15 with a "bomb" of size 4 results in: 4 new entities of 3 each, and a remainder of 3 that goes to the "trash"
    return entities, remainder

# 15 with 4bomb
# bombNumber(15, 4)


def simulateGameKindOf():
    # generate a list of random numbers, more likely to be square numbers, all at 25 or below (easy mode)
    listOfSquares = [1, 4, 9, 16, 25]
    listOfNumbers = []
    for x in range(8):
        listOfNumbers.append(random.randrange(1, 25))
        listOfNumbers.append(random.choice(listOfSquares))
    # print("playing with " + str(len(listOfNumbers)) + " numbers")
    totalTrash = 0
    entitiesSum = 0

    for x in range(len(listOfNumbers)):
        bomb = random.choice([2, 3, 4, 5])
        a, b = bombNumber(listOfNumbers[x], bomb)
        # print("a: " + str(a))
        # print("b: " + str(b))
        totalTrash += b
        for x in range(len(a)):
            entitiesSum += a[x]

    print(str(listOfNumbers))        
    print("entitiesSum: " + str(entitiesSum))
    print("entitiesSum / 5: " + str(entitiesSum / 5))
    print("totalTrash: " + str(totalTrash))



for x in range(4):
    simulateGameKindOf()
    print("")
