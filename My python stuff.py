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

