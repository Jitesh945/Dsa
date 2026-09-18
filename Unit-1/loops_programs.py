#1. Print numbers from 1 to 10 using a for loop.
print("assending order")
i=(1,2,3,4,5,6,7,8,9,10)
for x in i:
    print(x)

print("--------------------------")

#2 Print numbers from 10 to 1 using a while loop.

print("dissending order")
a=10

while a >= 1:
    print(a)
    a -= 1

print("-------------------------")
#3 Print the multiplication table of a number.

num = int(input("Enter a number for tables "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

print("-------------------------")


#4. Find the sum of numbers from 1 to n.

n1=int(input("enter number for sum:-"))

sum = 0

for i in range(1, n1 + 1):
    sum += i

print("Sum =", sum)

#5. Find the factorial of a number.

n = int(input("Enter your number for factor no:-"))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("Factorial number :-", factorial)



#6. Print all even numbers between 1 and 100.

for i in range(2, 101, 2):
    print(i)



#7. Reverse a number using a loop.


number = int(input("Enter your number for reverse "))

reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print(" your Reversed number :-", reverse)

#8 Count the digits of a number.

j= int(input("Enter digits number for counting "))

count = 0

while j > 0:
    j = j // 10
    count += 1

print("Number of digits =", count)

#9 Check whether a number is prime.

p = int(input("Enter a number for check prime or not:- "))

if p < 2:
    print("Not a prime number")
else:
    prime = True

    for i in range(2, p):
        if p % i == 0:
            prime = False
            break

    if prime:
        print("Prime number")
    else:
        print("Not a prime number")



#10 Print Fibonacci series up to n terms.


y = int(input("Enter number for fibonacci:- "))

h = 0
s = 1

for i in range(y):
    print(h, end=" ")
    h, s = s, h + s






