import re
words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

file = open("input.txt","r")
sum = 0
for line in file:
    line = line.strip()
    numArr = re.findall('\d', line)

    firstString = line[0:line.index(numArr[0])]
    secondString = line[line.rfind(numArr[-1])+1:]

    num1 = numArr[0]
    num2 = numArr[-1]

    if not firstString and not secondString:
        calc = str(num1) + str(num2)
        sum += int(calc)
        continue

    if any(ele in firstString for ele in words.keys()):
        ptr1 = 0
        ptr2 = 2
        while not any(ele in firstString[ptr1:ptr2] for ele in words.keys()):
            ptr2 += 1
        while any(ele in firstString[ptr1:ptr2] for ele in words.keys()):
            ptr1 += 1
        ptr1 -= 1
        num1 = words.get(firstString[ptr1:ptr2])

    if any(ele in secondString for ele in words.keys()):
        ptr1 = -2
        ptr2 = -1
        while not any(ele in secondString[ptr1:] for ele in words.keys()):
            ptr1 -= 1
        while any(ele in (secondString[ptr1:ptr2] if ptr2 < -1 else secondString[ptr1:ptr2]) for ele in words.keys()):
            ptr2 -= 1
        ptr2 += 1
        num2 = words.get(secondString[ptr1:]) if secondString[ptr1:ptr2] not in words.keys() else words.get(secondString[ptr1:ptr2])

    calc = str(num1) + str(num2)
    sum += int(calc)

    
print(sum)