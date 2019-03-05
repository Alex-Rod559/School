'''
spamm = input("type food: ")

if spamm == 'spamm':
    print('Ummmm, my favorite!')
    print('I feel like saying it 100 times...')
    print(100 * (spamm + '! '))
'''

# Established a reference dictionary of all available items
foodOptions = {
    "bread": 2.50,
    "crosants": 2.00,
    "cake": 4.50,
    "muffins": 1.50,
    "pie": 3.50,
    "cookie": 1.00
}


#ask for user input of the items they want 
FoodCollection = input("Plaese only select 5 of the following food items: bread, crosants, muffins, cake, pie, cookie \nType out the desired items seperated by a comma: ")

#converts everything into a list from the above input statems 
Food_List = FoodCollection.split(", ")




print("Printing Food")

for food in Food_List:
        print(food)

