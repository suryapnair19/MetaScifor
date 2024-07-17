#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Write a Python program to print 'Hello, World!'.


# In[2]:


print("Hello, World!")


# In[3]:


a= "'Hello, World!'"
print(a)


# In[4]:


#2. Write a Python program to add two numbers.


# In[5]:


a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = a+b
print("\n Sum of the numbers", a ," and ", b, " is ",c)


# In[6]:


#3. Write a Python program to find the square root of a number.


# In[7]:


import math


# In[8]:


a = int(input("Enter the number "))
c = math.sqrt(a)
print("The square root of ",a, "=", c)


# In[9]:


#4. Write a Python program to calculate the area of a triangle.


# In[10]:


def area(b, h):
    area = (b*h) /2
    print("\n Area of the triangle is ", area)
    return
b = int(input("Enter the baselength of the triangle: "))
h = int(input("enter the height of the triangle: "))
area(b,h)


# In[11]:


#5. Write a Python program to swap two variables.


# In[12]:


x = 10
y = 15
x,y = y,x
print(x,y)


# In[13]:


#6. Write a Python program to generate a random number.


# In[14]:


x = int(input("Enter a random number"))
print("\n The random number is: ", x)


# In[15]:


#7. Write a Python program to convert kilometers to miles


# In[16]:


km = float(input("Enter the kilometer "))
miles = km * 0.621371
print("\n\t",km,"km is equal to ",miles,"miles" )


# In[17]:


# 8. Write a Python program to check if a number is positive, negative or zero


# In[18]:


x = int(input("Enter the number"))
if x < 0:
    print(x," is negative.")

elif x > 0:
    print(x, " is positive")
else:
    print(x," is Zero")



# In[19]:


#9. Write a Python program to check if a number is odd or even


# In[20]:


x = int(input("Enter the number "))
if x%2 ==0:
    print(x, " is an even number")
else:
    print(x, " is an odd number")


# In[21]:


#10. Write a Python program to check if a year is a leap year.


# In[22]:


def leapyear(year):
    if year%4 ==0:
        print(year, " is a leap year")
    else:
        print(year, " is not a leap year")

year =int(input(" Enter the year "))
leapyear(year)
        



# In[23]:


#11. Write a Python program to find the largest of three numbers


# In[24]:


def larger(x,y,z):
    if x>y:
        if(x>z):
            print(x," is the larger")
    elif y>x:
        if y>z:
            print(y, " is the larger")
    else:
        print(z, " is the larger")

x =int(input(" Enter the 1st number"))
y =int(input(" Enter the 2nd number"))
z =int(input(" Enter the 3rd number"))
larger(x,y,z)


# In[25]:


##12. Write a Python program to find the factorial of a number


# In[ ]:





# In[ ]:





# In[ ]:





# In[26]:


#13. Write a Python program to display the multiplication table.


# In[27]:


for num in range(1,11):
    print("Multiplication table for",num)
    for i in range(1,11):
        print(num*i)
        if i ==10:
            print( "\n","*"*30 )
else:
    print("*" * 30)


# In[28]:


#14. Write a Python program to print the Fibonacci sequence


# In[29]:


num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
if num_terms < 0:
    print("Invalid input. Please enter a non-negative number.")
else:
    a, b = 0, 1
if num_terms >= 1:
    print(a)
if num_terms >= 2:
    print(b)
for i in range(2, num_terms):
    c = a + b
    print(c)
    a, b = b, c 


# In[30]:


#15. Write a Python program to check if a number is an Armstrong number.


# In[31]:


def armstrong(num):
    if num <= 0:
        print("Please enter a number greater than 0")
    n = num
    sums = 0
    no_of_digits = len(str(num)) 
    while num >0:
        ns = num% 10
        sums = sums + (ns ** no_of_digits)
        num = num/ 10
    
    if sums == n:
        print(n, "is an armstrong number")
    else:
        print(n, "is not an armstrong number")
    return
num = int(input("Enter the number"))
armstrong(num)


# In[ ]:





# In[32]:


# 16. Write a Python program to find the sum of natural numbers.


# In[33]:


def sum_of_natural_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

n = int(input("Enter a positive integer n: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    result = sum_of_natural_numbers(n)
    print(" The sum of first ", n, "natural numbers is ", result)



# In[34]:


#17. Write a Python program to find the sum of digits of a number.


# In[35]:


def sum_of_digits(num):
    sums = 0
    while num > 0:
        n = num % 10
        sums = sums + n
        num = num // 10
    return sums
num = int(input("enter the number "))
s = sum_of_digits(num)
print(s,"is the sum of the digits of the number: ",num)


# In[36]:


# 18. Write a Python program to reverse a number.


# In[37]:


def reverse_number(num):
    reversed_num = 0
    while num > 0:
        remainder = num % 10
        reversed_num = reversed_num * 10 + remainder
        num = num // 10
    return reversed_num
num = 12345
reversed_num = reverse_number(num)
print(f"The reverse of {num} is {reversed_num}")


# In[38]:


##19. Write a Python program to convert decimal to binary, octal and hexadecimal.


# In[39]:


def convert_decimal(number):
    binary = bin(number).replace("0b", "")

    octal = oct(number).replace("0o", "")

    hexadecimal = hex(number).replace("0x", "").upper()

    return binary, octal, hexadecimal

decimal_number = 345

binary, octal, hexadecimal = convert_decimal(decimal_number)

print(f"Decimal number: {decimal_number}")
print(f"Binary: {binary}")
print(f"Octal: {octal}")
print(f"Hexadecimal: {hexadecimal}")



# In[40]:


##20. Write a Python program to find HCF or GCD of two numbers


# In[41]:


def compute_hcf(x, y):
    smaller = min(x, y)
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

hcf = compute_hcf(num1, num2)
print("The HCF of", num1, "and", num2, "is", hcf)


# In[42]:


##21. Write a Python program to find LCM of two numbers.


# In[43]:


def find_lcm(a,b):
    
    larger = max(a, b)
    while True:
        if larger % a == 0 and larger % b == 0:
            lcm = larger
        break
    larger += 1
    return lcm

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(find_lcm(a,b))


# In[ ]:


##22. Write a Python program to count the number of each vowel in a string


# In[44]:


def count_vowels(text):
    vowel_counts = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    text = text.lower()
    for char in text:
        if char in vowel_counts:
            vowel_counts[char] += 1  # Increment count for that vowel
    return vowel_counts

text = input("Enter a string: ")

vowel_counts = count_vowels(text)

print("Vowel counts:")
for vowel, count in vowel_counts.items():
  print(f"{vowel}: {count}")


# In[ ]:


#23. Write a Python program to remove punctuation from a string.


# In[45]:


def remove_punctuation(text):
    punctuation = ".!\"#$%&()*+,/:;<=>?@[]^_`{|}~"
    no_punct_table = str.maketrans('', '', punctuation)
    return text.translate(no_punct_table)

text = input("Enter a string: ")

text_without_punct = remove_punctuation(text)

print("String without punctuation:", text_without_punct)


# In[ ]:


##24. Write a Python program to sort a list of numbers in ascending order.


# In[46]:


numbers = [3, 1, 4, 5, 2]

numbers.sort()

print("Sorted list:", numbers)


# In[ ]:


#  25. Write a Python program to merge two lists and sort it.


# In[ ]:


list1 = list[2, 98, 89, 23, 76, 12, 78]
list2 = list[56, 268, 9862, 23, 13, 134]
tlist = list1 + list2
slist = tlist.sort()
print("Merged and sorted list : ", slist)

