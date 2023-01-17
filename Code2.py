x=range(1,1001)
for number in x:

    if number%3==0 and number%5==0:
        print(number,"fizz-barr")
    elif number%3==0:
        print(number,"fizz")
    elif number%5==0:
        print(number,"barr")
    else:
        print (number)
