file = open('input.txt','r') 
raw_data = file.read().strip() 
first_packet_marker = 0 

# part b 
for index, value in enumerate (raw_data): 
    currentList = [i for i in raw_data[index:index+4]] 
    found_dupe = False 
    for listindex, listvalue in enumerate(currentList[:-1]): 
        if currentList[listindex] in currentList[listindex+1:len(currentList)]: 
                found_dupe = True 
                break 
    if found_dupe == False: 
            first_packet_marker = index + 4 
            break 
print(first_packet_marker) 

# part b 
first_packet_marker = 0 
for index, value in enumerate (raw_data): 
    currentList = [i for i in raw_data[index:index+14]] 
    found_dupe = False 
    for listindex, listvalue in enumerate(currentList[:-1]): 
        if currentList[listindex] in currentList[listindex+1:len(currentList)]: 
                found_dupe = True 
                break 
    if found_dupe == False: 
            first_packet_marker = index + 14 
            break 
print(first_packet_marker) 