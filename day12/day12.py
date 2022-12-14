from string import ascii_lowercase

elevation_map = open('input.txt','r').read().strip().split('\n')
letter_to_number = dict()
for i in ascii_lowercase:
    letter_to_number[i] = ascii_lowercase.index(i)
letter_to_number['S'] = 0
letter_to_number['E'] = 25

# part a
startCoord = []
for row in range(len(elevation_map)):
    for col in range(len(elevation_map[row])):
        if elevation_map[row][col] == 'S':
            startCoord = [row, col]
shortest_path = []
already_visited = [startCoord]
priority_queue = [[startCoord, [startCoord]]]

while(len(priority_queue) > 0):
    curr_node = priority_queue.pop(0)
    row = curr_node[0][0]; col = curr_node[0][1]
    curr_history = curr_node[1].copy()
    for dr, dc in [[0,1],[1,0],[0,-1],[-1,0]]:
        r = row + dr; c = col + dc
        if not (0 <= r < len(elevation_map) and 0 <= c < len(elevation_map[0])):
            continue
        if not (letter_to_number[elevation_map[r][c]] <= letter_to_number[elevation_map[row][col]] + 1):
            continue
        if [r, c] in already_visited:
            continue
        already_visited.append([r,c])
        new_history = curr_history.copy()
        new_history.append([r,c])
        priority_queue.append([[r, c], new_history])
        if elevation_map[r][c] == 'E':
            shortest_path = new_history
            priority_queue.clear()
            break
print(len(shortest_path) - 1)

# part b
startCoord = []
for row in range(len(elevation_map)):
    for col in range(len(elevation_map[row])):
        if elevation_map[row][col] == 'E':
            startCoord = [row, col]
shortest_path = []
already_visited = [startCoord]
priority_queue = [[startCoord, [startCoord]]]

while(len(priority_queue) > 0):
    curr_node = priority_queue.pop(0)
    row = curr_node[0][0]; col = curr_node[0][1]
    curr_history = curr_node[1].copy()
    for dr, dc in [[0,1],[1,0],[0,-1],[-1,0]]:
        r = row + dr; c = col + dc
        if not (0 <= r < len(elevation_map) and 0 <= c < len(elevation_map[0])):
            continue
        if not (letter_to_number[elevation_map[r][c]] >= letter_to_number[elevation_map[row][col]] - 1):
            continue
        if [r, c] in already_visited:
            continue
        already_visited.append([r,c])
        new_history = curr_history.copy()
        new_history.append([r,c])
        priority_queue.append([[r, c], new_history])
        if elevation_map[r][c] == 'a':
            shortest_path = new_history
            priority_queue.clear()
            break
print(len(shortest_path) - 1)
