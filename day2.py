info = open('information.txt','r') #replace information.txt with the name of your text file

def get_score(player, enemy) -> int: #check who would win in a rock-paper-scissors match
    score = 0
    
    if enemy == 'C' and player == 'X': #if enemy chose scissors
        score += 0 + 2 #player needs to loose
    elif enemy == 'C' and player == 'Y':
        score += 3 + 3 #player needs to draw
    elif enemy == 'C' and player == 'Z':
        score += 6 + 1 #player needs to win
    
    elif enemy == 'B' and player == 'X': #if enemy chose paper
        score += 0 + 1 #player needs to loose
    elif enemy == 'B' and player == 'Y':
        score += 3 + 2 #player needs to draw
    elif enemy == 'B' and player == 'Z':
        score += 6 + 3 #player needs to win
    
    elif enemy == 'A' and player == 'X': #if enemy chose rock
        score += 0 + 3  #player needs to loose
    elif enemy == 'A' and player == 'Y':
        score += 3 + 1 #player needs to draw
    elif enemy == 'A' and player == 'Z':
        score += 6 + 2 #player needs to win
    
    else:
        print('program has failed to run?')# shouldnt be printed
     
    return score
    
total_score = 0 
for line in info:
    enemy_play = line[0]
    your_play = line[2]
    score = get_score(your_play, enemy_play)


    total_score += score

print(total_score)
info.close()
