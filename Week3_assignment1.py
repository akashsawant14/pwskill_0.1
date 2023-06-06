#!/usr/bin/env python
# coding: utf-8

# ## Q1.Which keyword is used to create a function? Create a function to return a list of odd numbers in the range of 1 to 25.

# ### Ans - def keyword is used to create a fumction 

# In[32]:


def odd_num():
    l=[]
    for i in range(1,26):
        if i % 2 == 1:
            l.append(i)
    return l
        


# In[33]:


odd_num()


# ## Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs to demonstrate their use.

# ### Ans - *args is used to provide the arguments without knowning the number of arguments provided by use it returns tuple 
# ###  **kwargs is used to give the arguments in key value pair it returns dictionary

# In[37]:


def args_ex(*args):
    return args


# In[38]:


args_ex(2,2,3,4)


# In[39]:


args_ex(1,8,653,92,516,1617,919)


# In[41]:


type(args_ex())


# In[42]:


def kwargs_ex(**kwargs):
    return kwargs


# In[55]:


kwargs_ex(a='1',b='2',c='3')


# In[56]:


type(kwargs_ex())


# ### Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14,16, 18, 20].

# ### iterator is used to iter items over loop

# In[ ]:





# In[62]:


l=[2, 4, 6, 8, 10, 12, 14,16, 18, 20]

# __iter__() is used to iter items 
def iter(l):
    for i in range(0,5):
        print(l[i])
        
    


# In[110]:


c=iter(l)


# ### Q4.What is a generator function in python? Why yield keyword is used? Give an example of a generator function.

# ### Ans - Generator function is used to Generator-Function: A generator-function is defined like a normal function, but whenever it needs to generate a value
# ### Yield keyword is used to return the  values without using return keyword , and it is memory efficient

# In[ ]:





# In[ ]:





# In[82]:


def generator(a):
    for i in range(a):
        yield (i)


# In[83]:


for i in generator(10):
    print(i)


# ## Q5 Create a generator function for prime numbers less than 1000. Use the next() method to print the first 20 prime numbers.

# In[146]:


def find_primes():
    for num in range(2, 1000):
        is_prime = True
        for i in range(2, num):
            if (num % i) == 0:
                is_prime = False
                break
        if is_prime:
            yield num    


# In[147]:


prime_generator = find_primes()
for j in range(20):
    
    prime = next(prime_generator)
    print(prime)


# ### Q6.Write a python program to print the first 10 Fibonacci numbers using a while loop.

# In[162]:


def fib_series(n):
    a,b=0,1
    print(a)
    while n < 10:
        a,b=b,a+b
        n=n+1
        print(a)


# In[163]:


fib_series(0)


# ### Q7.Write a List Comprehension to iterate through the given string: ‘pwskills’.Expected output: ['p', 'w', 's', 'k', 'i', 'l', 'l', 's']

# In[115]:


s='pwskills'


# In[116]:


l=[x for x in s]


# In[117]:


l


# In[118]:


s='pwskills'
print([*s])


# ### Q8.Write a code to print odd numbers from 1 to 100 using list comprehension.

# In[109]:


l1=[i for i in range(1,100) if i%2==1]
print(l1)


# In[ ]:




