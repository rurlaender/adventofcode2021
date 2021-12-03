import math
nbrs = [0,0,0,0,0,0,0,0,0,0,0,0]
with open('data.txt', 'r') as data:
    for line in data:
        for i in range (0,12):
            if int(line,2) & int(math.pow(2,i)) == int(math.pow(2,i)) :
                nbrs[i] += 1
gamma=0
epsilon=0                
for i in range (0,12):
    if nbrs[i]>500:
        gamma += int(math.pow(2,i))
    else:
        epsilon += int(math.pow(2,i)) 
print(nbrs, gamma, epsilon, gamma*epsilon) 
        
