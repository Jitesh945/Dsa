#1.	Write a function to print "Hello, World!".

def msg():
    print("hello wolrd!")
msg()
print("-----------------------------")
#2.	Write a function that takes a name and prints a greeting.

def msg1(x):
    print(x)
msg1(10)
print("-----------------------------")


#3.	Write a function to add two numbers.

def add(x,y):
    print("sum:-",x+y)
add(10,20)
print("-----------------------------")

#4.	Write a function to find the square of a number.

def square(a):
    print("square of number:-",a*a)
square(5)

print("-----------------------------")

#5.	Write a function to check whether a number is even or odd.

def check(b):
    if(b % 2==0):
        print("b is even")
    else:
        print("b is odd")
check(19)
print("-----------------------------")

#6.	Write a function to find the maximum of two numbers.

def find(x,y):
    if(x>y):
        print("x is max")
    else:
        print("y is max")
find(23,54)

print("-----------------------------")

#7.	Write a function to convert Celsius to Fahrenheit.


def find1(m):
    print("celsius:-",m)
    n=m*9/5+32
    print("farenheit:-",n)

find1(50)

print("-----------------------------")

#8.	Write a function to calculate the area of a circle.
# a= 3.14 r*r


def find11(r):
    pai=3.14
    print("area of the circle is=",pai*r*r)
find11(5)
print("-----------------------------")

#9.	Write a function to calculate the factorial of a number.


def factor():
    n = int(input("Enter your number for factor no:-"))

    factorial = 1

    for i in range(1, n + 1):
        factorial *= i

    print("Factorial number :-", factorial)

factor()

print("-----------------------------")

#10.	Write a function to check whether a number is positive, negative, or zero.

def check(h):
    if(h>0):
        print("h is positive =",h)
    elif(h<0):
        print("h is negative =",h)
    else:
        print("h is zero =",h)

check(40)
print("-----------------------------")

#11.	Write a function to find the maximum of three numbers.

def find111(i,j,k):
    if i>j and i>k:
        print("i is max",i)
    elif j>i and j>k:
        print("j is max",j)
    else:
        print("k is max",k)
find111(12,36,32)

print("-----------------------------")

#12.	Write a function to count vowels in a string.

def vowel():
    s="Atmiya university"
    vowel=['a','e','i','o','u']
    count=0
    for i in range(len(s)):
        if (s[i] in vowel):
            count+=1
    print("vowel count=",count)
vowel()

print("-----------------------------")
#13.	Write a function to reverse a string.

def reverse():
    a="jitesh"
    print(a[::-1])
reverse()

#14.	Write a function to check whether a string is a palindrome.

def is_palindrome():

    a = input("Enter a string: ")
    return a == a[::-1]

if is_palindrome():
    print("Palindrome")
else:
    print("Not a palindrome")
print("-----------------------------")

#15.	Write a function to find the sum of all elements in a list.


def total():
    l = [1, 2, 3, 4, 5]
    print("list:-", l)
    ans = sum(l)
    return ans

print("total:-", total())

print("-----------------------------")


#16.	Write a function to find the largest element in a list.

def largest():
    l = [10, 255, 5, 40, 15]
    print("list:-", l)

    ans = l[0]

    for i in range(len(l)):
        if l[i] > ans:
            ans = l[i]

    return ans

print("largest:-", largest())

print("-----------------------------")

#17.	Write a function to remove duplicate elements from a list.


def duplicates():
    l = [10,15,20,20,25,30,30]
    print("original list:-", l)

    ans = []

    for i in l:
        if i not in ans:
            ans.append(i)

    return ans

print("list without duplicates:-", duplicates())

print("-----------------------------")

#18.	Write a function to count how many times an element appears in a list.



def count_element():
    l = [15, 25, 25, 35, 25, 44, 55]
    element = 25
    count = 0

    print("list:-", l)

    for i in l:
        if i == element:
            count += 1

    return count

print("count:-", count_element())

print("-----------------------------")

#19.	Write a function to check whether a number is prime.


def prime():
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
prime()
print("-----------------------------")


#20.	Write a function to return all prime numbers between two numbers.

def prime1():
    no1=int(input("enter a first number:-"))
    no2=int(input("enter a second number:-"))

    if no1<=1 or no2<=1:
        prime=False
    else:
        for i in range(no1,no2):
            prime=True
            for j in range(2,i):
                if i%j ==0:
                    prime=False
            if prime:
                print(i," is prime number")

prime1()
print("-----------------------------")


#21.	Write a function to calculate Fibonacci numbers.



y = int(input("Enter number for fibonacci:- "))

h = 0
s = 1

for i in range(y):
    print(h, end=" ")
    h, s = s, h + s


print("-----------------------------")
print("-----------------------------")


#22.	Write a function to find the second-largest number in a list.


def sec(numbers):
    print("your list",nums)
    uni = list(set(numbers))
    uni.sort(reverse=True)
    return uni[1]

nums = [10, 20, 4, 45, 99]
print("your second larger number is",sec(nums))  

print("-----------------------------")

#23.	Write a function to sort a list without using sort().


def sort111(numbers):
    print("your unsorted list:-",nums)
    n = len(numbers)

    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


nums = [5, 2, 8, 1, 3]
print("your sorted list",sort111(nums))

print("-----------------------------")


#24.	Write a function to merge two lists and remove duplicates.


def merge(list1, list2):
    print("your first list:-",list1)
    print("your second list:-",list2)
    result = []

    for item in list1 + list2:
        if item not in result:
            result.append(item)

    return result


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

print(merge(list1, list2))

print("-----------------------------")













