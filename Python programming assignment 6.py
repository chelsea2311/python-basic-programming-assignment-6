#!/usr/bin/env python
# coding: utf-8

# PYTHON PROGRAMMING ASSIGNMENT NO. 6

# DISPLAY FIBONACCI SEQUENCE USING RECCURSION

# In[3]:


def fibonacci(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(n):
        a,b=b,a+b
        print(b)
fibonacci(5)        


# In[5]:


fibonacci(8)


# FACTORIAL OF NUMBER USING RECURSION

# In[7]:


def recursion(num):
    fact = 1
    for i in range(num,0,-1):
        fact=i*fact
    print(fact)
recursion(3)


# In[8]:


recursion(7)


# BODY MASS INDEX

# In[9]:


weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in meters: "))
BMI = weight/(height*2)
print(BMI)


# NATURAL LOGARITHM OF ANY NUMBER

# In[10]:


import numpy
n = float(input("Enter any number: "))
l = numpy.log(n)
print(l)


# CUBE SUM OF N NATURAL NUMBERS

# In[11]:


n = int(input("Enter any number: "))
sum = (n*(n+1)/2)**2
print("Cube sum of first",n,"natural numbers is: ",sum)


# In[ ]:




