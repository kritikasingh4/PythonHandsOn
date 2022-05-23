#!/usr/bin/env python
# coding: utf-8

# # ACTIVITY 1 

# # 1. sum of 2 numbers

# In[1]:


a = int(input("enter first number: "))
b = int(input("enter second number: "))
sum = a + b
print("sum:", sum)


# #  2. print hello world

# In[2]:


print ('Hello world')


# # 3.  find square root
# 

# In[7]:


num=float(input("enter number to find square root : "))
num_sqrt=num**0.5
print("square root: ", num_sqrt)


# # 4. find area of a triangle
# 

# In[9]:


height=int(input("Enter height value of triangle: "))
base=int(input("Enter base value of triangle: "))
area=0.5*height*base
print("Area of the triangle is: ", area)


# # 5. solving a quadratic equation

# In[12]:


import cmath
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
d=(b*b)-(4*a*c)
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print("the solution:", sol1, sol2)


# # 6. swap 2 variables

# In[13]:


x=10
y=50
x,y=y,x
print("The value of x is: ",x)
print("The value of y is" ,y)


# # 7. generate a random number

# In[14]:


import random
n=random.random()
print(n)


# # 8. to convert kms to miles

# In[2]:


kil = float (input ("Enter distance in kms: "))  
conversion_ratio= 0.621371  
mil = kil* conversion_ratio 
print ("Distance in miles ", mil)  


# # 9. Convert Celsius to Farenheit

# In[4]:


celsius=float(input("Enter temperature in celsius: "))
farenheit = (celsius * 9/5) + 32
print("Temperature in Fareheint is: ", farenheit)


# # 10. print output without a newline

# In[5]:


print("Python", end=" ")
print("is easy to learn.")


# # ACTIVITY 2

# # 1. to check if number is positive, negative or 0 

# In[9]:


num=int(input("Enter the number to be checked: "))
if num>0:
    print("The number is positive")
elif num==0:
    print("The number is zero")
else :
    print("The number is negative")


# # 2. to check if a numbr is odd or even

# In[12]:


num=int(input("Enter a number: "))
if num%2==0:
    print("The number is even")
else:
    print("The number is odd")


# # 3. to check for leap year

# In[14]:


year=int(input("Enter the year: "))
if year%4==0:
    print("The year is a leap year!!")
else:
    print("Its not a leap year :(")


# # 4. to check for largest among entered numbers

# In[17]:


num1=float(input("Enter the first number"))
num2=float(input("Enter the second number"))
num3=float(input("Enter the third number"))

if(num1>num2) and (num1>num3):
    print("First number is the largest.")
elif(num2>num1) and (num2>num3):
    print("Second number is the largest.")
else:
    print("Third number is the largest.")
    


# # 5. to check prime number

# In[19]:


num=int(input("Enter a number: "))
if num>1:
    for i in range(2, num):
        if(num%2)==0:
            print(num,"is not a prime number.")
            break
    else:
        print(num,"is a prime number.")
else:
    print(num,"is a not prime number")


# # 6. print all prime numbers in an interval

# In[23]:


lower_val=int(input("Enter the lower range value: "))
upper_val=int(input("Enter the upper range value: "))
print ("The Prime Numbers in the range are: ")  
for number in range (lower_val, upper_val + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  


# # 7. factorial of a number

# In[1]:


num=int(input("Enter a number: "))
factorial=1
if num<0:
    print("Sorry, factorial doesnt exist for neagative numbers.")
elif(num==0):
    print("Factorial od 0 is 1.")
else:
    for i in range(1, num+1):
        factorial=factorial*i
    print("The factorial of",num,"is",factorial)


# # 8. multiplication table

# In[2]:


num=int(input("Enter the number for multiplication table: "))
for i in range(1,11):
    print(num,"*",i,"=",num*i)
    


# # 9. fionacci series

# In[4]:


nterms=int(input("Enter the number of terms: "))
n1, n2=0,1
count=0
if(nterms<=0):
    print("Please enter a positive integer: ")
elif(nterms==1):
    print("Fibonacci series upto",nterms,":")
    print(n1)
else:
    print("Fibonacci series:")
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1


# # 10. armstrong number
# 

# In[7]:


num=int(input("Enter the number: "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
    
if num==sum:
    print(num,"is an armstrong number.")
else:
    print(num,"isnt an armstrong number.")


# # 11. find armstrong number in an interval

# In[10]:


lower = 100
upper = 2000

for num in range(lower, upper + 1):
   order=len(str(num))
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
   if num == sum:
       print(num)


# # 12. sum of natural numbers

# In[11]:


num=int(input("Enter the number to calculate the sum: "))
num=(num*(num+1))/2
print("The sum of the numbers is",num)


# # 13. pyramid patterns

# In[17]:


rows=int(input("Enter the number of rows: "))
for i in range(rows,0,-1):
    for j in range(0,i):
        print("^",end=" ")
    print("\n")


# # 14. iterate over dictionaries using for loop

# In[19]:


dt={'vada':'pav', 'chole':'samose'}
for key in dt:
    print(key, dt[key])


# # 15. reverse a number

# In[20]:


num=int(input("Enter a number to be reversed: "))
print(str(num)[::-1])


# # 16. compute the power of a number

# In[23]:


base=int(input("Enter the base value: "))
exponent=int(input("Enter the exponent value: "))
result=pow(base, exponent)
print("Answer is:"+str(result))


# # ACTIVITY 3
# 

# # 1. display powers of 2 using anynymous function

# In[2]:


terms=int(input("Enter the number of terms: "))
result=list(map(lambda x:2**x, range(terms)))
print("Total terms are: ",terms)
for i in range(terms):
    print("2 power",i,"is",result[i])


# # 2. find numbers divisible by other numbers

# In[3]:


mylist=[13, 34, 65, 107, 117, 130]
result=list(filter(lambda x:(x%13==0), mylist))
print("Numbers divisible by 13 are: ",result)


# # 3. Convert Decimal to Binary, Octal and Hexadecimal

# In[6]:


dec=int(input("Enter a decimal value: "))
print(bin(dec),"in binary.")
print(oct(dec),"in octal.")
print(hex(dec),"in hexadecimal.")


# # 4. find ASCII value of character

# In[10]:


c = 'p'
print("The ASCII value of '" + c + " is", ord(c))


# # 5. find HCF or GCD

# In[13]:


def compute_hcf(x,y):
    while(y):
        x,y=y,x%y
        return x
hcf=compute_hcf(300,400)
print("The HCF is",hcf)


# # 6. find LCM

# In[23]:


def compute_lcm(x, y):

   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

print("The L.C.M. is", compute_lcm(num1, num2))


# # 7. find factors of a number

# In[30]:


def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = int(input("Enter the number to find its factors:"))

print_factors(num)


# # 8. simple calculator

# In[2]:


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break 
          
    
    else:
        print("Invalid Input")


# # 9. shuffle a deck of cards

# In[3]:


import itertools, random
deck=list(itertools.product(range(1,14),['spade', 'heart', 'diamond', 'club']))

random.shuffle(deck)

print("You got:")
for i in range(5):
    print(deck[i][0], "of", deck[i][1])


# # 10. display calendar

# In[6]:


import calendar

yy=int(input("Enter year: "))
mm=int(input("Enter month: "))

print(calendar.month(yy,mm))


# # 11. fibonacci series using recursion

# In[8]:


def recur_fibo(n):
    
    if n<=1:
        return n
    else:
        return( recur_fibo(n-1)+recur_fibo(n-2))
    
nterms=5

if nterms<=0:
    print("Please enter a positive integer: ")
else:
    print("Fibonacci series: ")
    for i in range(nterms):
        print(recur_fibo(i))


# # 12. sum of natural numbers using recursion

# In[10]:


def recur_sum(n):
    if n<=0:
        return n
    else:
        return n+ recur_sum(n-1)
    
num=int(input("Enter a number:"))

if num<0:
    print("Enter a positive number please.")

else:
    print("The sum is: ", recur_sum(num))


# # 13. find factorial using recursion

# In[22]:


def recur_factorial(n):
    if n==1:
        return n
    else:
        return n*recur_factorial(n-1)

num=int(input("Enter a number: "))

if num<0:
    print("Please enter a positive number.")
    
elif num==0:
    print("Factorial of 0 is 1.")
    
else:
    print("Factorial of", num, "is: ", recur_factorial(num))


# # 14. convert decimal to binary using recursion

# In[24]:


def converttobinary(n):
    if n>1:
        converttobinary(n//2)
    print(n%2, end=' ')
    
dec=int(input("Enter a decimal: "))

converttobinary(dec)
print()


# # 15. return mutliple values from a function 

# In[27]:


def name():
    n1=str(input("Enter a name: "))
    n2=str(input("Enter another name: "))
    n3=str(input("Enter a name: "))
    
    return{1:n1, 2:n2, 3:n3}
names=name()
print(names)


# # ACTIVITY 4

# # 1. sum of arrays

# In[28]:


arr=[]
arr=[1,568,4566,9000,789]
ans=sum(arr)
print("The sum is: ", ans)


# # 2. largest element in array

# In[34]:


def largest(arr,n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
        return max

arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr,n)
print ("Largest in given array is",Ans)   


# # 3. array rotation

# In[ ]:




