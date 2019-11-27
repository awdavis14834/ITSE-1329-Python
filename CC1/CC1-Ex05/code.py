from random import choice
food = choice(['banana', 'chicken', 'corn', 'baseball'])
if food == 'banana' :
    print('Fruit')
elif food == 'chicken' :
    print('Meat')
elif food == 'corn' :
    print('Vegetable')
else :
    print('Could not verify food')