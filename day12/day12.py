import string
elevation_map = open('input.txt','r').read().strip().split('\n')
letter_to_number = dict()

letter_to_number['E'] = 27
for i in string.ascii_lowercase:
    letter_to_number[i] = string.ascii_lowercase.index(i) + 1
letter_to_number['S'] = 0

# part a
startCoord = []
for row in range(len(elevation_map)):
    for col in range(len(elevation_map[row])):
        if letter_to_number[elevation_map[row][col]] == 0:
            startCoord = [row, col]

shortest_path = []
already_visited = [startCoord]
priority_queue = [[startCoord, [startCoord]]]

while(len(priority_queue) > 0):
    curr_node = priority_queue.pop(0)
    row = curr_node[0][0]
    col = curr_node[0][1]
    curr_history = curr_node[1].copy()
    if col < len(elevation_map[0]) - 1 and [row, col + 1] not in already_visited and letter_to_number[elevation_map[row][col + 1]] < letter_to_number[elevation_map[row][col]] + 2:
        curr_history_copy = curr_history.copy()
        curr_history_copy.append([row, col + 1])
        priority_queue.append([[row, col + 1], curr_history_copy])
        already_visited.append([row, col + 1])
        if elevation_map[row][col + 1] == 'E':
            shortest_path = curr_history_copy
            break
    if row < len(elevation_map) - 1    and [row + 1, col] not in already_visited and letter_to_number[elevation_map[row + 1][col]] < letter_to_number[elevation_map[row][col]] + 2:
        curr_history_copy = curr_history.copy()
        curr_history_copy.append([row + 1, col])
        priority_queue.append([[row + 1, col], curr_history_copy])
        already_visited.append([row + 1, col])
        if elevation_map[row + 1][col] == 'E':
            shortest_path = curr_history_copy
            break
    if col > 0                         and [row, col - 1] not in already_visited and letter_to_number[elevation_map[row][col - 1]] < letter_to_number[elevation_map[row][col]] + 2:
        curr_history_copy = curr_history.copy()
        curr_history_copy.append([row, col - 1])
        priority_queue.append([[row, col - 1], curr_history_copy])
        already_visited.append([row, col - 1])
        if elevation_map[row][col - 1] == 'E':
            shortest_path = curr_history_copy
            break
    if row > 0                         and [row - 1, col] not in already_visited and letter_to_number[elevation_map[row - 1][col]] < letter_to_number[elevation_map[row][col]] + 2:
        curr_history_copy = curr_history.copy()
        curr_history_copy.append([row - 1, col])
        priority_queue.append([[row - 1, col], curr_history_copy])
        already_visited.append([row - 1, col])
        if elevation_map[row - 1][col] == 'E':
            shortest_path = curr_history_copy
            break


# almost working....

# startCoord = []
# for row in range(len(elevation_map)):
#     for col in range(len(elevation_map[row])):
#         if letter_to_number[elevation_map[row][col]] == 27:
#             startCoord = [startCoord]

# shortest_path = []
# already_visited = [startCoord]
# priority_queue = [[startCoord, [startCoord]]]

# while(len(priority_queue) > 0):
#     curr_node = priority_queue.pop(0)
#     row = curr_node[0][0]
#     col = curr_node[0][1]
#     curr_history = curr_node[1].copy()
#     if col < len(elevation_map[0]) - 1 and [row, col + 1] not in already_visited and letter_to_number[elevation_map[row][col + 1]] > letter_to_number[elevation_map[row][col]] - 2 and letter_to_number[elevation_map[row][col + 1]] < letter_to_number[elevation_map[row][col]] + 2:
#         curr_history_copy = curr_history.copy()
#         curr_history_copy.append([row, col + 1])
#         priority_queue.append([[row, col + 1], curr_history_copy])
#         already_visited.append([row, col + 1])
#         if elevation_map[row][col + 1] == 'a':
#             shortest_path = curr_history_copy
#             break
#     if row < len(elevation_map) - 1    and [row + 1, col] not in already_visited and letter_to_number[elevation_map[row + 1][col]] > letter_to_number[elevation_map[row][col]] - 2 and letter_to_number[elevation_map[row + 1][col]] < letter_to_number[elevation_map[row][col]] + 2:
#         curr_history_copy = curr_history.copy()
#         curr_history_copy.append([row + 1, col])
#         priority_queue.append([[row + 1, col], curr_history_copy])
#         already_visited.append([row + 1, col])
#         if elevation_map[row + 1][col] == 'a':
#             shortest_path = curr_history_copy
#             break
#     if col > 0                         and [row, col - 1] not in already_visited and letter_to_number[elevation_map[row][col - 1]] > letter_to_number[elevation_map[row][col]] - 2 and letter_to_number[elevation_map[row][col - 1]] < letter_to_number[elevation_map[row][col]] + 2:
#         curr_history_copy = curr_history.copy()
#         curr_history_copy.append([row, col - 1])
#         priority_queue.append([[row, col - 1], curr_history_copy])
#         already_visited.append([row, col - 1])
#         if elevation_map[row][col - 1] == 'a':
#             shortest_path = curr_history_copy
#             break
#     if row > 0                         and [row - 1, col] not in already_visited and letter_to_number[elevation_map[row - 1][col]] > letter_to_number[elevation_map[row][col]] - 2 and letter_to_number[elevation_map[row - 1][col]] < letter_to_number[elevation_map[row][col]] + 2:
#         curr_history_copy = curr_history.copy()
#         curr_history_copy.append([row - 1, col])
#         priority_queue.append([[row - 1, col], curr_history_copy])
#         already_visited.append([row - 1, col])
#         if elevation_map[row - 1][col] == 'a':
#             shortest_path = curr_history_copy
#             break




printedMap = []
for i in range(len(elevation_map)):
    newRow = []
    for j in range(len(elevation_map[i])):
        if [i, j] in shortest_path:
            newRow.append('#')
        else:
            newRow.append(elevation_map[i][j])
    printedMap.append(newRow)

fileOut = open('output.txt', 'w')
for line in printedMap:
    strLine = ""
    for i in line:
        strLine += i
    fileOut.write(strLine)
    fileOut.write('\n')
    print(strLine)

print(len(shortest_path) - 1)
print(shortest_path)