hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
try:
    if float(hours) > 40 :
        ot = float(hours) - 40
        otr = float(rate) * 1.5
        otpay = 40 * float(rate) + float(ot) * float(otr)
        print('Pay:', float(otpay))
    else :
        pay = float(hours) * float(rate)
        print('Pay:', float(pay))
except:
    print('Error, please enter numeric input')
    quit()