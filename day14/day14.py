# get wall sections
wall_sections = open('input.txt','r').read().strip().split('\n')
walls = []
for wall in wall_sections:
    chunks = wall.split(" -> ")
    for chunk in range(1, len(chunks)):
        curr_chunk = list(map(int, chunks[chunk].split(',')))
        prev_chunk = list(map(int, chunks[chunk - 1].split(',')))
        dx = abs(curr_chunk[0] - prev_chunk[0])
        dy = abs(curr_chunk[1] - prev_chunk[1])
        if dx > 0:
            for i in range(dx + 1):
                walls.append([min(curr_chunk[0], prev_chunk[0]) + i, curr_chunk[1]])
        if dy > 0:
            for i in range(dy + 1):
                walls.append([curr_chunk[0], min(curr_chunk[1], prev_chunk[1]) + i])
# print(min([x for x in walls[0]]))
min_x = (min(things[0] for things in walls))
min_y = (min(things[1] for things in walls))
print(min_x)
print(min_y)