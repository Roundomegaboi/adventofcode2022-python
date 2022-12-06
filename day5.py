'''This code will solve the second problem challenge for day 5, however it can be adapted to solve the first'''

filename = 'information.txt' #change this to the name of the file 
info = open(filename,'r') 
crates = [[i] for i in range(10)] 
counter = 0
row = 0
groups = info.readlines()[8] #the first 8 lines contain the initial order of the crates
info.close()


info = open(filename,'r')

for i in range(8): #loop through the first 8 lines and create a 2d list representing the containers
    line = info.readline()
    for index, letter in enumerate(line):
        if letter.isupper():
            try:
                group = int(groups[index])
                crates[group].append(letter)
            except:
                pass
            
        else:
            pass
        
print('')
info.close()
info = open(filename,'r')
crates.remove([0])

for line in info.readlines()[10:]: #reorder the containers
    line = line.replace('\n','')
    amount = int(line[4:line.find(' ',5)].strip())
    from_index = line.index('from') + 5
    starting_column = int(line[from_index:line.index(' ',from_index)])
    final_column = int(line[-1])
    
    moving = crates[starting_column-1][1:amount+1]
    for i in moving[::-1]:
        crates[final_column-1].insert(1,i)
        
    for i in moving:
        crates[starting_column-1].remove(i)
        
        
        
for i in crates: print(i[1],end='',sep='') #print top container on each pile after reordering has completed.
info.close()
