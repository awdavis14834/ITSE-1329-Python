#Aaron Davis
count = 1 #this gives a base number for the number of greetings
while True: #this while loop lets the code ask for multiple greetings
    #main variables
    first = input('What is your first name?: ')
    last = input('What is your last name?: ')
    initial = last[:1]
    time = input('What time of day is it?(Morning, Afternoon, Evening): ')
    #this determines what the output will be, based on variable inputs
    if time == 'Morning':
        print('Have a good breakfast,',first,initial)
    elif time == 'Afternoon':
        print('Have a good lunch,',first,initial)
    elif time == 'Evening':
        print('Have a good dinner,',first,initial)
    else:
        print('Have a good one,',first,initial)
    #this part determines whether or not the loop restarts or ends, based on input    
    answer = input('would you like another greeting?: ')
    if answer == 'yes':
        count = count +1 #this will update the number of greetings that are recieved
        continue
    elif answer == 'no':
        break
    #this just states how many greetings the code has ran
print('You recieved'+' '+str(count)+' '+'greetings')