# Draw numbers for each player
import random

# make player list
names = ["Nate", "Sam", "Ali","Beth", "Andy", "Alex"]

# numbers pot
num_list = list(range(1, len(names) + 1))


# draw numbers for each player
new_dict = {}
for name in names:
    
    num = random.choice(num_list)
    num_list.remove(num)
    new_dict[name] = num

## Open a Present ##

# make presents list
presents = ["Box of Chocolates", "Beer Mug", "Dog Poster", "Bottle of Wine", "Farside Calendar"]

# assign random present to each player
present_dict = {}
while len(presents) > 0:
    for name in names:
        if new_dict[name] == min(new_dict.values()):
            chosen_present = random.choice(presents)
            present_dict[name] = chosen_present
            presents.remove(chosen_present)

print(present_dict)