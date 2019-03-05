#Author: Alexander Rodriguez 
#3/5/2019
#Program: Allows users to pick the amount of something and it outputs how much they got and how much it cost 

#Ask for users to input the desired amount for each item 
cake1 = int(input("Type amount of Cakes you want: "))
pie1 = int(input("Type amount of Pies you want: "))
cookies1 = int(input("Type amount of Cookies you want: "))
bread1 = int(input("Type amount of Loafs of bread you want: "))
muffins1 = int(input("Type amount of Muffins you want: "))

#Establishes how much each item cost 
cake_price = cake1 * 3 
pie_price = pie1 * 6
cookie_price = cookies1 * 2
bread_price = bread1 * 4
muffins_price = muffins1 * 5

#Produccess dicount 
discountCake = cake_price * .2
discountPie = pie_price * .3
discountCookie = cookie_price * .5
discountBread = bread_price * .4
discountMuffin = muffins_price * .1

#adds everything into their own variable to facilitate formating
dicountList = ('20%','30%','50%','40%','10%')
item_price = (cake_price, pie_price, cookie_price, bread_price, muffins_price)
quant = cake1, pie1, cookies1, bread1, muffins1
items = ('Cake', 'Pie', 'Cookies', 'Bread', 'Muffins')
discountTotal = discountBread + discountCake + discountCookie + discountMuffin + discountPie 

#Prints the headers for the output 
print ("%4s %16s %16s %20s" % \
    ("Item", "Quantity","Selling Price", "Discount in Percent"))

#Calls all the reference variables from above so that it can populate the list with proper values, *zip() helps with the proper formating of the code*
for item, quantity, price, discount in zip(items, quant , item_price, dicountList):
    print("%-7s%12s%13s%14s" % \
        (item, quantity, price, discount))

#prints out the total to the second decimal. 
print ("Total: $ %0.2f" % discountTotal)
