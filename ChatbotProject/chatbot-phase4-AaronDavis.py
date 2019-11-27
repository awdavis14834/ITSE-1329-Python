#Aaron Davis
def greeter():
    """This function takes input about a person's name and the time of day,
    and returns a greeting based on that input, it also counts the number of greetings"""
    import random as rand
    time = rand.randint(1,24)
    print('The current hour is', time)
    #this determines what the output will be, based on variable inputs
    if 5 <= time <= 10:
        return'Have a good breakfast,'+' '+first+' '+initial
    elif 11 <= time <=15:
        return'Have a good lunch,'+' '+first+' '+initial
    elif 16 <= time <= 20:
        return'Have a good dinner,'+' '+first+' '+initial
    else:
        return'Have a good one,'+' '+first+' '+initial
            
       

count = 1 #this gives a base number for the number of greetings
while True: #this while loop lets the code ask for multiple greetings
        #main variables
    first = input('What is your first name?: ')
    last = input('What is your last name?: ')
    initial = last[:1]
    print(greeter())
    answer = input('would you like another greeting?: ')
    if answer == 'yes':
        count = count +1 #this will update the number of greetings that are recieved
        continue
    elif answer == 'no':
        break
    #this just states how many greetings the code has ran
print('You recieved '+ str(count)+ ' greetings')
