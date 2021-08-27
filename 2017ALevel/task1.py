inventoryf = open('INVENTORY.txt', 'r')
Inventory = [itemstack.strip() for itemstack in inventoryf]  # all list
ItemTypes = list(set(Inventory))
ItemCounts = [sum([(itemstack == item) for itemstack in Inventory]) for item in ItemTypes]
inventoryf.close()
print('ItemType             Count')
[print('{0:<20} {1}'.format(ItemTypes[i], ItemCounts[i])) for i in range(len(ItemTypes))]