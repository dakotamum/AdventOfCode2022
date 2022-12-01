def partA(inputs):
    currentSum = 0
    maxCalories = 0

    for i in range(len(inputs)):
        if inputs[i] == '' or i == len(inputs) - 1:
            if(i == len(inputs) - 1):
                currentSum += int(inputs[i])
            if currentSum > maxCalories:
                maxCalories = currentSum
            currentSum = 0
        else:
            currentSum += int(inputs[i].strip("\n"))
    print("-------- PART A --------")
    print(maxCalories)

def partB(inputs):
    currentSum = 0
    firstPlace = 0
    secondPlace = 0
    thirdPlace = 0

    for i in range(len(inputs)):
        if inputs[i] == '' or i == len(inputs) - 1:
            if i == len(inputs) - 1:
                currentSum += int(inputs[i])
            if currentSum > firstPlace:
                thirdPlace = secondPlace
                secondPlace = firstPlace
                firstPlace = currentSum
            elif currentSum > secondPlace:
                thirdPlace = secondPlace
                secondPlace = currentSum
            elif currentSum > thirdPlace:
                thirdPlace = currentSum
            currentSum = 0
        else:
            currentSum += int(inputs[i].strip("\n"))

    sum = firstPlace + secondPlace + thirdPlace
    print("-------- PART B --------")
    print(sum)

file = open('input.txt','r')
inputs = []
for line in file:
    if line != '':
        inputs.append(line.strip("\n"))

partA(inputs)
partB(inputs)