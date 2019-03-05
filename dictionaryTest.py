prices = {}  

aa = 5.  
bb = 4.  
cc = 10.  
dd = 3.  
ee = 5.  
ff = 4.  

prices['shrimp'] = aa
prices['groundbeef'] = bb
prices['tuna'] = cc
prices['sodapop'] = dd
prices['fruitplate'] = ee
prices['spicerack'] = ff

# other stuff here ...

item1 = input("To begin, please enter an item name:") #item2 input

price1 = prices[item1]

item2 = input("Now, add a second item:")

price2 = prices[item2]

item3 = input("Finally, add your last item:") #item3 input

price3 = prices[item3]

print (price1, price2, price3)