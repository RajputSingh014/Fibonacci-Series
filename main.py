#Variables
a=0
b=1
#Taking Input
x=int(input("Enter the no.of Fibonacci to be generated: "))
print(x)
#Checking The Input
if x<=0:
    print("The entered value must be positive!, Try Again")
elif x==1:
    print(x)
#Generating the Fibonacci Series
elif x>=2:
    print("{},{}".format(a,b), end='')
    for i in range (2,x):
        c=a+b
        print(",{}".format(c), end='')
        a=b
        b=c
    
