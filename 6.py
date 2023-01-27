a=int(input("Enter Value 'a' : "))
b=int(input("Enter Value 'b' : "))
c=int(input("Enter Value 'c' : "))
D= b*b-4*a*c
print (D)
if D>0:
    print ("Real And Distint Roots")
elif D==0:
    print ("Real And Equal Roots")
elif D<0:
    print ("Imaginary Roots")
