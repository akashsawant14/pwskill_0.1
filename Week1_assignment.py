#!/usr/bin/env python
# coding: utf-8

# # Q1. Create one variable containing following type of data:

# In[75]:


#(i) string
var1= 'Akash'
#(ii) list
list1=[1,2,'Sawant','Mu-Sigma']
#(iii) float
float1= 2.45454
#(iv) tuplE
tuple1 = (1,2,'PWSKILL')


# In[76]:


print(var1)
print(list1)
print(float1)
print(tuple1)


# ## Q2. Given are some following variables containing data:
# ### (i) var1 = ‘ ‘
# ### (ii) var2 = ‘[ DS , ML , Python]’
# ### (iii) var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]
# ### (iv) var4 = 1.
# ### What will be the data type of the above given variable.

# In[77]:


var1 = ''
# ans -- str


# In[78]:


type(var1)


# In[79]:


var2 = '[ DS , ML , Python]'
#ans --- str


# In[80]:


type(var2)


# In[81]:


var3 = [ 'DS' , 'ML' , 'Python' ]
# ans --- list


# In[82]:


type(var3)


# In[83]:


var4=1.
# ans -- float


# In[84]:


type(var4)


# ## Q3. Explain the use of the following operators using an example:
# ### (i) /
# ### (ii) %
# ### (iii) //
# ### (iv) **

# In[85]:


#(i) / 
# ans its dividion airthmatic operator and returns division of equation

# example 
int(10/2)


# In[86]:


#(ii) %
# ans its modulus airthmatic operator and returns reminder

# example 
(10%3)


# In[87]:


#(iii) //
# ans its floor division airthmatic operator and returns floor dividon

# example 
(14//3)


# In[88]:


#(iv) **
# ans its power airthmatic operator and power of number

# example 
4**3


# ## Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the
# ## element and its data type.

# In[89]:


list2 = [1,2,3.454,'akash','sawant','kiran',[1,2,3],{'a':'akash','b':1},(1,2),'string']


# In[90]:


len(list2)


# In[91]:


for i in list2:
    print(type(i))


# ## Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how manytimes it can be divisible.

# In[92]:


a=10
b=2
c=a%b


# In[93]:


while b>a:
    print(a//b)
else:
    print(a//b)


# ## Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is divisible by 3 or not.

# In[94]:


q6= [25]
for i in q6:
    if (i % 3 ==0):
        print("Element is dividible by 3")
    else:
        print("Element is not dividible")


# ## Q7. What do you understand about mutable and immutable data types? Give examples for both showing this property.

# In[95]:


# mutable 
# Ans -- Mutable property is the property where we can change or modify the data type elements using its indexes 
  # Eg - List is mutable i.e we can modify the elements from list using indexes


# In[96]:


# immutable 
 # we can not change or modify the data type using indexes 
    # eg . string is immutable i.e we can nott modify string using its indexes


# In[97]:


#mutable example
mut_list = [1,2,4,6]


# In[98]:


mut_list[2]='akash'


# In[99]:


mut_list


# In[100]:


#immutable example

str1='akash'


# In[101]:


str1[2]= 'w'


# In[ ]:




