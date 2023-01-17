# Code For Checking The BMI (Body Mass Index)..................
x=float(input("Enter Your Weight : "))
# Your Weight......
print (x,"Kg Is Your Weight") 
y=float(input("Enter Your Height : "))
# Your Height...
print (y, "M Is Your Height.")
B=x/y*1/y

print (B)
# Your BMI........
if B<19.9:
    print ("Underweight")
elif 20<B<24.9:
    print("Normal")
elif 25<B<29.9:
    print("Overweight")
elif B>30:
    print("Obese")
# THANKYOU.........................^_^