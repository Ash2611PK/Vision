x=range(1,51)
for number in x:
    if number%2==0 and number%5==0 :
        print (number,"Hunt-Parkour")
    elif number%2==0:
        print (number,"Hunt")
    elif number%5==0:
        print(number,"Parkour")
    else :
        print(number)