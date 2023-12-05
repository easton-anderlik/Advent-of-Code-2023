import numpy
def scoreCard(winningNumbers, myNumbers):
    score = 0
    for num in myNumbers:
        if num in winningNumbers:
            if not score:
                score = 1
            else:
                score *= 2
    return score

def numberRight(winningNumbers, myNumbers):
    number = 0
    for num in myNumbers:
        if num in winningNumbers:
            number += 1
    return number


file = open("input.txt", "r")
contents = file.readlines()
numberOfCopies = numpy.ones(len(contents), numpy.int_)
#print(numberOfCopies)

#runningScore = 0
for line in contents:
    print(line)
    card = line.strip().split(":")[0].split(" ")[1]
    winningNumbers = list(filter(None, line.strip().split(":")[1].split("|")[0].split(" ")))
    myNumbers = list(filter(None, line.strip().split(":")[1].split("|")[1].split(" ")))
    print("Card: ", card)
    number = numberRight(winningNumbers, myNumbers)
    print("Number Winning: ", number, "")
    #score = scoreCard(winningNumbers, myNumbers)
    #print("Score: ", score, "\n")
    for i in range(number):
        #print(i)
        print("Adding ", numberOfCopies[int(card)-1], " copies to ", int(card)+i+1)
        numberOfCopies[int(card)+i] += numberOfCopies[int(card)-1]
    print()


    #runningScore += score
totalCards = 0
for num in numberOfCopies:
    print(num)
    totalCards+=num
print("Total: ", totalCards)