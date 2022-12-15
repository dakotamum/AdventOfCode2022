from functools import cmp_to_key

def inOrder(thing1, thing2):
    if isinstance(thing1, int) and isinstance(thing2, int):
        if thing1 < thing2:
            return 1
        elif thing1 > thing2:
            return -1
        else:
            return 0
    if (isinstance(thing1, int)):
        thing1 = [thing1]
    if (isinstance(thing2, int)):
        thing2 = [thing2]

    iter = 0
    while iter < len(thing1) and iter < len(thing2):
        order = inOrder(thing1[iter], thing2[iter])
        if order == 1:
            return 1
        elif order == -1:
            return -1
        iter += 1
    
    if iter == len(thing1) and len(thing1) == len(thing2):
        return 0
    if iter == len(thing1):
        return 1
    return -1

# part a
raw_pairs = open('input.txt','r').read().strip().split("\n\n")
sum_ordered = 0
for index, pair in enumerate(raw_pairs):
    thing1, thing2 = map(eval, pair.split('\n'))
    order = inOrder(thing1, thing2)
    if order == 1 or order == 0:
        sum_ordered += index + 1
    
print(sum_ordered)

# part b
list_of_packets = list(map(eval, open('input.txt','r').read().strip().replace("\n\n", '\n').split('\n')))

list_of_packets.append([[2]])
list_of_packets.append([[6]])
list_of_packets = sorted(list_of_packets, key=cmp_to_key(inOrder), reverse=True)

index_a = 0; index_b = 0
for index, listy in enumerate(list_of_packets):
    if listy == [[2]]:
        index_a = index + 1
    if listy == [[6]]:
        index_b = index + 1

print(index_a * index_b)