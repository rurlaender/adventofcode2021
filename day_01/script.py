first_line = True
counter = 0
last_nbr = 0
nbrs = []
with open('data.txt', 'r') as data:
    for line in data:
        nbr  = int(line)
        nbrs.append(nbr)
        
for i in range(1,2000):
    if nbrs[i]>nbrs[i-1]:
        counter += 1
print(counter)

counter = 0
for i in range(0,1997):
    a = nbrs[i]+ nbrs[i+1] + nbrs[i+2]
    b = nbrs[i+1]+ nbrs[i+2] + nbrs[i+3]
    if  b > a:
        counter +=1
           
print(counter) 
