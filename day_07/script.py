class crab_boot():
    def __init__(self, start_pos, linear=True):
        self.start_pos = start_pos
        self.linear = linear
    
    def calc_fuel(self, target_pos):
        fuel = 0
        if self.linear:
            fuel = abs(self.start_pos-target_pos)
        else:
            steps = abs(self.start_pos-target_pos)
            #Do some math ;)
            fuel = int((steps*(steps+1))/2)
        return fuel

input=[]

with open("data.txt", "r") as data:
    for line in data:
        input_str = line.split(',')
for i_str in input_str:
    input.append(int(i_str))

crabs = []
for pos in input:
    crabs.append(crab_boot(pos,False))
    
    
min_val = min(input)
max_val = max(input)

fuel_cost = []

for i in range(min_val ,max_val+1):
    fuel = 0
    for crab in crabs:
        fuel += crab.calc_fuel(i)
    fuel_cost.append(fuel)
print(min(fuel_cost))
