murections = open('input.txt','r').read().strip().split("\n")

# part a
currentHead = [0, 0]
currentTail = [0, 0]
positionsTailVisited = []
positionsTailVisited.append(currentTail)
for move in murections:
	direction, steps = move.split(" ")
	for i in range(int(steps)):
		previousHead = currentHead.copy()
		if direction == 'R':
			currentHead[0] += 1
		elif direction == 'L':
			currentHead[0] -= 1
		elif direction == 'U':
			currentHead[1] += 1
		else:
			currentHead[1] -= 1
		coordDiff = [currentHead[0] - currentTail[0], currentHead[1] - currentTail[1]]
		if abs(coordDiff[0]) > 1 or abs(coordDiff[1]) > 1:
			currentTail = previousHead
			if currentTail not in positionsTailVisited:
				positionsTailVisited.append(currentTail)
print(len(positionsTailVisited))

# part b
currentCoords = []
for i in range(10):
	currentCoords.append([0, 0])
positionsTailVisited = []
positionsTailVisited.append([0, 0])
for move in murections:
	direction, steps = move.split(" ")
	for i in range(int(steps)):
		alreadyMadeBigMove = False
		bigMove = [0, 0]
		previousHead = currentCoords[0].copy()
		if direction == 'R':
			currentCoords[0][0] += 1
		elif direction == 'L':
			currentCoords[0][0] -= 1
		elif direction == 'U':
			currentCoords[0][1] += 1
		else:
			currentCoords[0][1] -= 1
		for knot in range(1, len(currentCoords)):
			knot_previous_head = currentCoords[knot].copy()
			coordDiff = [currentCoords[knot - 1][0] - currentCoords[knot][0], currentCoords[knot - 1][1] - currentCoords[knot][1]]
			if abs(coordDiff[0]) > 1 or abs(coordDiff[1]) > 1: # we need to make a change
				if abs(coordDiff[0]) + abs(coordDiff[1]) > 2:    # we need to make a beeg change
					if alreadyMadeBigMove:
						currentCoords[knot][0] += bigMove[0]
						currentCoords[knot][1] += bigMove[1]
					else:
						alreadyMadeBigMove = True
						bigMove = [previousHead[0] - currentCoords[knot][0], previousHead[1] - currentCoords[knot][1]]
						currentCoords[knot] = previousHead
				else:
					alreadyMadeBigMove = False
					bigMove = [0, 0]
					currentCoords[knot] = [currentCoords[knot][0] + int((coordDiff[0])/2), currentCoords[knot][1] + int((coordDiff[1])/2)]
			else:
				alreadyMadeBigMove = False
				bigMove = [0, 0]
			previousHead = knot_previous_head.copy()
		if currentCoords[9] not in positionsTailVisited:
			positionsTailVisited.append(currentCoords[9].copy())
print(len(positionsTailVisited))
