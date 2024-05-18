#input of the two numbers
a = float(input("Enter the first number = "))
b = float(input("Enter the second number = "))

#calculations to be done
print("for sumation press 1")
print("for substraction press 2")
print("for multiplication press 3")
print("for division press 4")

#name of the calculation
c = int(input("what you want to do "))
while True :
     if c<1 or c>4 :
            print()
            c = int(input("what you want to do "))
     else :
            break
     
#calculations
if c == 1 :
    print ("the sumation is ", a + b)
elif c == 2 :
    print("the sustraction is ", a - b)
elif c == 3:
    print("the multiplication is ", a * b)
else :
    print("the division is ", a / b)