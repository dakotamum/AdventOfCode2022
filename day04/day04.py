# part a
file = open('input.txt','r')
raw_data = file.read().split("\n")
all_encapsulated_sum = 0

# part a
for section_assignment_pair in raw_data:
    section1_range = section_assignment_pair.split(',')[0].split('-')
    section2_range = section_assignment_pair.split(',')[1].split('-')
    section1 = list(range(int(section1_range[0]), int(section1_range[1]) + 1))
    section2 = list(range(int(section2_range[0]), int(section2_range[1]) + 1))
    if all(i in section2 for i in section1) or all(i in section1 for i in section2):
        all_encapsulated_sum += 1
print(all_encapsulated_sum)

# part b
all_encapsulated_sum = 0
for section_assignment_pair in raw_data:
    section1_range = section_assignment_pair.split(',')[0].split('-')
    section2_range = section_assignment_pair.split(',')[1].split('-')
    section1 = list(range(int(section1_range[0]), int(section1_range[1]) + 1))
    section2 = list(range(int(section2_range[0]), int(section2_range[1]) + 1))
    if any(i in section2 for i in section1) or any(i in section1 for i in section2):
        all_encapsulated_sum += 1
print(all_encapsulated_sum)
