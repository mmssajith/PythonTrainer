"""
This program is to identify the first unique item in a list
"""

def firstUniqueItem(products):
  counts = {}

  for product in products:
    if product in counts:
      counts[product] += 1
    else:
      counts[product] = 1

  for product in products:
    if counts[product] == 1:
      return product
    
  return None

list = ["Computer", "Apple", "Computer", "Apple", "Bag"]
print(firstUniqueItem(list))
