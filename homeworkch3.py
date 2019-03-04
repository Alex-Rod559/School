'''
spamm = input("type food: ")

if spamm == 'spamm':
    print('Ummmm, my favorite!')
    print('I feel like saying it 100 times...')
    print(100 * (spamm + '! '))
'''



FoodCollection = input("Plaese only select 5 of the following food items: Bread, Crosants, Muffins, Cake, Pie, Cookie \nType out the desired items seperated by a comma: ")
Food_List = FoodCollection.split(", ")



#Pushthisbitch

print("Printing Food")
for food in Food_List:
    print(food)

#QuantCollection = int(input("Plesae type how many of "))