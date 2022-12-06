file = open('input.txt','r')
raw_data = file.read()
stack_data, instruction_data = raw_data.split("\n\n")
stacks_data_separated = list(stack_data.split('\n'))
instruction_data_separated = list(instruction_data.split('\n'))
col_numbers_string = stacks_data_separated.pop(-1)
col_number_positions = []

for index, val in enumerate(col_numbers_string):
    if val != ' ':
        col_number_positions.append(index)

# part a
stacks = [[] for i in range(len(col_number_positions))]
for i in stacks_data_separated:
    for j, val in enumerate(col_number_positions):
        if i[val] != " ":
            stacks[j].append(i[val]) 

for line in instruction_data_separated:
    line_separated = line.split(' ')
    num_things_to_move = int(line_separated[1])
    col_to_move_from = int(line_separated[3])
    col_to_move_to = int(line_separated[5])
    for i in range(num_things_to_move):
        stacks[col_to_move_to - 1].insert(0, stacks[col_to_move_from - 1].pop(0))

answer = ""
for i in stacks:
    answer += i[0]
print(answer)

# part b
stacks = [[] for i in range(len(col_number_positions))]
for i in stacks_data_separated:
    for j, val in enumerate(col_number_positions):
        if i[val] != " ":
            stacks[j].append(i[val]) 

for line in instruction_data_separated:
    line_separated = line.split(' ')
    num_things_to_move = int(line_separated[1])
    col_to_move_from = int(line_separated[3])
    col_to_move_to = int(line_separated[5])
    for i in range(num_things_to_move):
        stacks[col_to_move_to - 1].insert(0, stacks[col_to_move_from - 1].pop(num_things_to_move - i - 1))

answer = ""
for i in stacks:
    answer += i[0]
print(answer)