info = open('information.txt','r') #replace information.txt with the name of your text file

totals = []
total = 0
for i in info:
    number = i
    if number == '\n':
        totals.append(total)
        total = 0
    else:
        total += int(number)
    

biggest1 = 0 
biggest2 = 0 #second biggest
biggest3 = 0 #third biggest

for i in totals:
    if i > biggest1:
        biggest1 = i

totals.remove(biggest1)

for i in totals:
    if i > biggest2:
        biggest2 = i

totals.remove(biggest2)

for i in totals:
    if i > biggest3:
        biggest3 = i

print(biggest1, biggest2, biggest3) 

    
print(totals)

info.close()
