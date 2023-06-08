#!/usr/bin/env python
# coding: utf-8

# ### Q1.Create a python program to sort the given list of tuples based on integer value using a lambda function.

# In[42]:


marks=[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]


# In[43]:


marks.sort(key=lambda x :x[1])


# In[44]:


marks


#  ### Write a Python Program to find the squares of all the numbers in the given list of integers using lambda and map functions.

# In[45]:


l2=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[46]:


list(map(lambda x:x**2,l2))


# ### Write a python program to convert the given list of integers into a tuple of strings. Use map andlambda functions
# Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')

# In[47]:


l3=  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[53]:


# str(tuple(l3))


# In[54]:


tuple(map(lambda x: str(x),l3))


# ### Write a python program using reduce function to compute the product of a list containing numbers from 1 to 25.

# In[77]:


l1=[i for i in range(1,26)]


# In[ ]:





# In[78]:


from functools import reduce


# In[79]:


(reduce(lambda x,y:x*y,l1))


# ### Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the  filter function.

# In[88]:


l4=[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]


# In[89]:


list(filter(lambda x : x%2 ==0 and x%3 ==0  ,l4))


# ### Write a python program to find palindromes in the given list of strings using lambda and filter function.

# In[90]:


l5=['python', 'php', 'aba', 'radar', 'level']


# In[92]:


list(filter(lambda x : x[0:]==x[::-1],l5))


# In[ ]:




