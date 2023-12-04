import re

def substring_range(s, substring):
    pattern = r'(?<!\d)' + re.escape(substring) + r'(?!\d)'
    for i in re.finditer(pattern, s):
        yield (i.start(), i.end())

def contains_special_character(s):
    pattern = r'[@/!#$%&*\-+=]'
    return re.search(pattern, s)

def contains_star(s):
    pattern = r'[*]'
    return re.search(pattern, s)


file = open("input.txt", "r")
fileArr = open("input.txt", "r").readlines()

prevLine = ""
line = file.readline().strip()
nextLine = file.readline().strip()

runningTotal = 0
starMap = {}
lineIndex = 0
while True:
    numLine = re.sub(r'[\D]+', " ", line)
    
    #make arr of nums
    f = filter(None, numLine.split(" "))
    numArr = list(f)

    for num in numArr:
        #if num in numArr[:lineIndex:]:
            #continue
        for value in substring_range(line, num):
            minIndex = max(value[0]-1, 0)
            maxIndex = min(value[1]+1, len(line))

            prevSubstring = "" if not prevLine else prevLine[minIndex:maxIndex:].strip()
            curSubstring = line[minIndex:maxIndex:].strip()
            nextSubstring = nextLine[minIndex:maxIndex:].strip()
            totalString = prevSubstring + curSubstring + nextSubstring
            star_index = contains_star(totalString)
            if star_index:
                #print(lineIndex)
                #print(totalString)
                #print(star_index)
                if contains_star(prevSubstring):
                    #print("Previous Line: ", lineIndex-1, "Position: ", minIndex+star_index.start())
                    #print(fileArr[lineIndex-1][minIndex+star_index.start()])

                    if (lineIndex-1, minIndex+star_index.start()) not in starMap.keys():
                        starMap[(lineIndex-1, minIndex+star_index.start())] = {num}
                    elif isinstance(starMap[(lineIndex-1, minIndex+star_index.start())],set):
                        starMap[(lineIndex-1, minIndex+star_index.start())].add(num)
                    
                    
                elif contains_star(curSubstring) :
                    #print("Line: ", lineIndex, "Position: ", minIndex+star_index.start()-len(prevSubstring))
                    #print(fileArr[lineIndex][minIndex+star_index.start()-len(prevSubstring)])
                    if (lineIndex, minIndex+star_index.start()-len(prevSubstring)) not in starMap.keys():
                        starMap[(lineIndex, minIndex+star_index.start()-len(prevSubstring))] = {num}
                    elif isinstance(starMap[(lineIndex, minIndex+star_index.start()-len(prevSubstring))], set):
                        starMap[(lineIndex, minIndex+star_index.start()-len(prevSubstring))].add(num)
                    

                elif contains_star(nextSubstring) :
                    #print("Next Line: ", lineIndex+1, "Position: ", minIndex+star_index.start()-(len(prevSubstring) + len(curSubstring)))
                    #print(fileArr[lineIndex+1][minIndex+star_index.start()-(len(prevSubstring) + len(curSubstring))])

                    if (lineIndex+1, minIndex+star_index.start()-(len(prevSubstring) + len(curSubstring))) not in starMap.keys():
                        starMap[(lineIndex+1, minIndex+star_index.start()-(len(prevSubstring) + len(curSubstring)))] = {num}
                    elif isinstance(starMap[(lineIndex+1, minIndex+star_index.start()-(len(prevSubstring) + len(curSubstring)))], set):
                        starMap[(lineIndex+1, minIndex+star_index.start()-(len(prevSubstring) + len(curSubstring)))].add(num)
                
            #print(totalString)
            #if contains_special_character(totalString):
                #print("Adding " + num + " to " + str(runningTotal))
            #    runningTotal+=int(num)

    lineIndex += 1

    
    #update lines
    prevLine = line
    line = nextLine
    nextLine = file.readline().strip()
    if not line:
        break
    #print(nextLine)
#print(starMap)
gearSum = 0
for key in starMap.keys():
    if len(starMap[key]) == 2:
        values = starMap[key]
        print(values)
        product = 1
        for val in values:
            product *= int(val)
        gearSum += product
print(gearSum)
#print(lineIndex)

