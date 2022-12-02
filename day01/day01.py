file = open('input.txt','r')
raw_data = file.read().strip()
elves = raw_data.split("\n\n")
caloric_totals = []

for elf in elves:
    calories = list(map(int, elf.split()))
    caloric_totals.append(sum(calories))

# part a
print(max(caloric_totals))
# part b
print(sum(sorted(caloric_totals)[-3:]))