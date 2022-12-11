datas = open('input.txt','r').read().strip().split("\n\n")
monkeys = []
for monkey in datas:
    monkeyDict = {} 
    monkeyString = monkey.split('\n')
    monkeyDict['current_items'] = list(map(int, monkeyString[1].strip("Starting items: ").split(',')))
    monkeyDict['operation'] = [monkeyString[2].split(' ')[5], monkeyString[2].split(' ')[6], monkeyString[2].split(' ')[7]]
    monkeyDict['test'] = int(monkeyString[3].split(' ')[-1])
    monkeyDict['true_case'] = int(monkeyString[4].split(' ')[-1])
    monkeyDict['false_case'] = int(monkeyString[5].split(' ')[-1])
    monkeyDict['num_items_inspected'] = 0
    monkeys.append(monkeyDict)

# part a
for iter in range(20):
    for i in range(len(monkeys)):
        while len(monkeys[i]['current_items']) > 0:
            item = monkeys[i]['current_items'].pop(0)
            operand = item if monkeys[i]['operation'][2] == "old" else int(monkeys[i]['operation'][2])
            item = int(item * operand) if monkeys[i]['operation'][1] == '*' else item + operand
            item = int(item / 3)
            if item % monkeys[i]['test'] == 0:
                monkeys[monkeys[i]['true_case']]['current_items'].append(item)
            else:
                monkeys[monkeys[i]['false_case']]['current_items'].append(item)
            monkeys[i]['num_items_inspected'] += 1

top_two_active = sorted([monkey['num_items_inspected'] for monkey in monkeys])[-2:]

print(top_two_active[0] * top_two_active[1])

# part b
lcm = 1
for monkey in monkeys:
    lcm *= monkey['test']

for iter in range(10000):
    for i in range(len(monkeys)):
        while len(monkeys[i]['current_items']) > 0:
            item = monkeys[i]['current_items'].pop(0)
            operand = item if monkeys[i]['operation'][2] == "old" else int(monkeys[i]['operation'][2])
            item = int(item * operand) if monkeys[i]['operation'][1] == '*' else item + operand
            item = int(item % lcm)
            if item % monkeys[i]['test'] == 0:
                monkeys[monkeys[i]['true_case']]['current_items'].append(item)
            else:
                monkeys[monkeys[i]['false_case']]['current_items'].append(item)
            monkeys[i]['num_items_inspected'] += 1
top_two_active = sorted([monkey['num_items_inspected'] for monkey in monkeys])[-2:]

print(top_two_active[0] * top_two_active[1])