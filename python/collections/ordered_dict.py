from collections import OrderedDict
numItems = int(input())
inventory = OrderedDict()

for i in range(numItems):
    item, space, amount = input().rpartition(' ')
    inventory[item] = inventory.get(item, 0) + int(amount)
    
for item in inventory:
    print(item, inventory[item])
