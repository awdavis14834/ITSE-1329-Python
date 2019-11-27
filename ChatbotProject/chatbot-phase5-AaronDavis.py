#Aaron Davis
def greeter():
    """This function takes input about a person's name and the time of day,
    and returns a greeting based on that input, it also counts the number of greetings"""
    import random as rand
    time = rand.randint(1,24)
    print('The current hour is', time)
    #this determines what the output will be, based on variable inputs
    if 5 <= time <= 10:
        meal = 'breakfast'
        count[meal] = count.get(meal, 0) +1
        return'Have a good breakfast,'+' '+first+' '+initial
    elif 11 <= time <=15:
        meal = 'lunch'
        count[meal] = count.get(meal, 0) +1
        return'Have a good lunch,'+' '+first+' '+initial
    elif 16 <= time <= 20:
        meal = 'dinner'
        count[meal] = count.get(meal, 0) +1
        return'Have a good dinner,'+' '+first+' '+initial
    else:
        meal = 'night'
        count[meal] = count.get(meal, 0) +1
        return'Have a good night,'+' '+first+' '+initial
            
       

count = {} 
while True: 
    first = input('What is your first name?: ')
    last = input('What is your last name?: ')
    initial = last[:1]
    print(greeter())
    answer = input('would you like another greeting?: ')
    if answer == 'yes':
        continue
    elif answer == 'no':
        for k,v in count.items():
            print(k,v)
        break
    

