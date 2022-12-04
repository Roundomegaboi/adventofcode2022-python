def split_line(line) -> tuple:
    dash_index = line.find('-')
    comma_index = line.find(',')
    
    num1 = line[0:dash_index]
    num2 = line[dash_index+1:comma_index]
    return int(num1), int(num2)

total_second_star = 0
total_first_star = 0
info = open('information.txt','r')

for line in info:
    num1, num2 = split_line(line)
    num3, num4 = split_line(line[line.find(',')+1:])
    
    if num1 == num2:
        first_set = {num1} 
    else:
        first_set = set(range(num1,num2+1))
    
    if num3 == num4:
        second_set = {num3}
    else:
        second_set = set(range(num3,num4+1))
        
    if first_set.issubset(second_set) or second_set.issubset(first_set):
        total_first_star += 1
        
    if first_set.intersection(second_set):
        total_second_star += 1

print(f'The answer for the first star is: {total_first_star}')
print(f'The answer for the second star is: {total_second_star}')
info.close()
