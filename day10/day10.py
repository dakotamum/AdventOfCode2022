instructions = open('input.txt','r').read().strip().split('\n')
x = 1
xpos = 0
xvalues = []
current_x_to_add = 0
wait = False
allDone = False
crt = [[' '] * 40 for i in range(6)]
while(not allDone):
    current_iter_row = int(xpos / 40)
    current_iter_col = xpos % 40
    if x > current_iter_col - 2 and x < current_iter_col + 2:
        crt[current_iter_row][current_iter_col] = u"\u2588"
    if not wait: # ready to grab next instruction
        inst = instructions.pop(0).split(' ')
        if inst[0] != "noop":
            current_x_to_add = int(inst[1])
            wait = True
    else:
        x += current_x_to_add
        wait = False
    xvalues.append(x)
    if (len(instructions) == 0 and not wait):
        allDone = True
    xpos += 1

# part a
print(xvalues[18]*20 + xvalues[58]*60 + xvalues[98]*100 + xvalues[138]*140 + xvalues[178]*180 + xvalues[218]*220)

# part b
for row in crt:
    row_string = ""
    for i in row:
        row_string += i
    print(row_string)