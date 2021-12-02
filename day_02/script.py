length = 0
depth = 0
with open('data.txt', 'r') as data:
    for line in data:
        cmd, val = line.split(' ')
        val=int(val)
        if 'forward' in cmd:
            length += val
        if 'down' in cmd:
            depth += val
        if 'up' in cmd:
            depth -= val
            
print(f'Length : {length}  Dept: {depth} Result: {length*depth}')

length = 0
depth = 0
aim = 0     
with open('data.txt', 'r') as data:
    for line in data:
        cmd, val = line.split(' ')
        val=int(val)
        if 'forward' in cmd:
            length += val
            depth += aim * val
        if 'down' in cmd:
            aim += val
        if 'up' in cmd:
            aim -= val
print(f'Length : {length}  Dept: {depth} Result: {length*depth}')
