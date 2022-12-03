# part a
file = open('input.txt','r')
raw_data = file.read().split("\n")
priority_sum = 0
for ruck_sack in raw_data:
    ruck_size = len(ruck_sack)
    first_half = ruck_sack[:ruck_size//2]
    second_half = ruck_sack[ruck_size//2:]
    for i in first_half:
        if(i in second_half):
            priority = ord(i) - ord('a') + 1 if ord(i) > 96 else ord(i) - 38
            priority_sum += priority
            break
print(priority_sum)

# part b
file = open('input.txt','r')
raw_data = file.read().split("\n")
priority_sum = 0
grouped_raw_data = []
# for i in raw_data:
while len(raw_data) > 0:
    grouped_raw_data.append(raw_data[:3])
    del raw_data[:3]
for group in grouped_raw_data:
    for i in group[0]:
        if all(i in string for string in group):
            priority = ord(i) - ord('a') + 1 if ord(i) > 96 else ord(i) - 38
            priority_sum += priority
            break
print(priority_sum)
