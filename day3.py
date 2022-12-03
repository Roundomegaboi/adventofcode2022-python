#part 1
info = open('information.txt','r') #change information.txt to the name of your puzzel input
total = 0
for line in info:
    compartment_size = int((len(line.replace('\n','')) / 2) + 0.5)  #split the string into 2 halves
    compartment1 = line[:compartment_size]
    compartment2 = line[compartment_size:].replace('\n','') 
    
    for letter in compartment1: #loop through each letter the first half and check if the letter is in the second half
        if letter in compartment2:
            if letter.isupper():
                total += ord(letter) - 38
                break
            elif letter.islower():
                total += ord(letter) - 96
                break
            
            else:
                print('broken') #shouldn't get printed
                exit()
print(total )
info.close()

#part 2
info = open('information.txt','r') #change information.txt to the name of your puzzle input
total = 0
group = [] 
for line in info: 
    group.append(line.replace('\n','')) #program adds line to list until the list has 3 items in it. The list then is representative of 1 'group'.
    if len(group) >= 3:
        for letter in group[0]: #we loop through each letter in the first string in the list. 
            if letter in group[1] and letter in group[2]: #if the letter is in both other strings in the list, we have found the common letter
                if letter.isupper(): 
                    total += ord(letter) - 38 
                    break
                
                elif letter.islower():
                    total += ord(letter) - 96
                    break
                    
                else:
                    print('Program has broke?') #shouldn't get printed
                    exit()
        group = []

print(total)
info.close()
