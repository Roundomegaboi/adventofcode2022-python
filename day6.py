#this solves the second challenge, can be adapted easily to solve the first.
filename = 'information.txt'
info = open(filename,'r')
data = info.readline()

chars = [data[i] for i in range(14,0,-1)] 

chars_processed = 4
for item in data[4:]:
    if len(set(chars)) == 14:
        break
        
    else:
        chars_processed += 1
        chars.pop()
        chars.insert(0,item)

    
