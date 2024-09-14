# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n=int(input())
item_dict=OrderedDict()

for i in range(n):
    item,price=input().strip().rsplit(' ',1)
    price=int(price)
    
    if item in item_dict:
        item_dict[item]+= price
    else:
        item_dict[item]=price
        
for item,price in item_dict.items():
    print(item,price)
        
        
