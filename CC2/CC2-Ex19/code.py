num = 0
tot = 0
while True:
    number = input('Enter a number: ')
    if number == 'done' :
        break
    try:
        inum = int(number)
    except:
        print('Invalid input')
        continue
    num = num + 1
    tot = tot + inum
print(tot,num,tot/num)
    