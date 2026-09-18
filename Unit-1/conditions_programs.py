#1 Check whether a number is positive, negative, or zero.

a=int(input("enter a:-"))
if(a>0):
    print("a is positive")
elif(a<0):
    print("a is negative")
else:
    print("a is zero")

print("-------------------------")

#2Check whether a person is eligible to vote.

age=int(input("enter age:-"))
if(age>18):
    print("you are eligible for vote")
else:
    print("you are not eligible for vote")


print("-------------------------")

#3 Find the largest of three numbers.

x=int(input("enter x:-"))
y=int(input("enter y:-"))
z=int(input("enter z:-"))

if x >= y and x >= z:
    print("Largest number:", x)
elif y >= x and y >= z:
    print("Largest number:", y)
else:
    print("Largest number:", z)

print("-------------------------")

#4. Check whether a year is a leap year.

year=int(input("enter year:-"))

if(year % 4==0):
    print("year is leap")
else:
    print("year is not leap year")

print("-------------------------")


#5 Create a grade system based on marks.

mark=int(input("enter mark:-"))

if(mark>=90):
    print("grade a")
elif(mark>=75):
    print("grade b")
else:
    print("grade c")
    
print("-------------------------")

#6Check whether a number is divisible by 5 and 11.

number=55

if number % 5 == 0 and number % 11 == 0:
    print("The number is divisible by both 5 and 11")
else:
    print("The number is not divisible by both 5 and 11")

print("-------------------------")

#7. Create a simple calculator using if-elif-else.


j = int(input("Enter first number: "))
p = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", j + p)
elif operator == "-":
    print("Result:", j - p)
elif operator == "*":
    print("Result:", j * p)
elif operator == "/":
    if p != 0:
        print("Result:", j / p)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")










