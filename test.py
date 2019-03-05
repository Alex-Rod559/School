
items = ('cake', 'pie', 'cookies', 'bread', 'muffins')


cake1 = int(input("Type amount of cakes you want: "))
pie1 = int(input("Type amount of pies you want: "))
cookies1 = int(input("Type amount of cookies you want: "))
bread1 = int(input("Type amount of loafs of bread you want: "))
muffins1 = int(input("Type amount of muffins you want: "))

quant = cake1, pie1, cookies1, bread1, muffins1

cake_price = cake1 * 3 
pie_price = pie1 * 6
cookie_price = cookies1 * 2
bread_price = bread1 * 4
muffins_price = muffins1 * 5

item_price = (cake_price, pie_price, cookie_price, bread_price, muffins_price)

discountCake = cake_price * .2
discountPie = pie_price * .3
discountCookie = cookie_price * .5
discountBread = bread_price * .4
discountMuffin = muffins_price * .1

dicountList = ('20%','30%','50%','40%','10%')

print ("%4s %16s %-16s %20s" % \
    ("Item", "Quantity","Selling Price", "Discount in Percent"))


for item, quantity, price, discount in zip(items, quant , item_price, dicountList):
    print("%-7s%16s%18s%14s" % \
        (item, quantity, price, discount))



