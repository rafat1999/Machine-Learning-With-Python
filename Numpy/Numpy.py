#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World")


# In[2]:


import numpy
arr = numpy.array([1,2,3,4])

print(arr)
print(type(arr))


# In[3]:


import numpy as np
t=(1,2,3,4,5.5)
arr = np.array(t)
print(arr)


# In[2]:


import numpy as np


# In[8]:


# different dimantion
# 0-D array

arr = np.array(42)
print(arr)
print(arr.ndim)

# 1-D array
arr1 = np.array([1,2,3])
print(arr1)
print(arr1.ndim) # nim is use for know the dimention

# 2-D array
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)
print(arr2.ndim)

# 3-D array

arr3 = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])
print(arr3)
print(arr3.ndim) 


# In[15]:


arr4 = np.array([1,2,3,4,5], ndmin=6) #ndim is use for higer dimention array
print(arr4)
print('No of dimantion: ',arr4.ndim)


# In[16]:


arr = np.array([10,11,5,8])
print(arr[2])
print(arr[0] + arr[1])


# In[18]:


arr = np.array([[1,2,3,4,10],[5,6,7,8,9]])
print("Last element from 1st element: ",arr[0, 4])
print("Last element from 2nd element: ", arr[1, -1])
print("Last element from 2nd element: ", arr[-1, -1])


# In[20]:


# Slicing Array

l = [10,20,30,40,50,60,70,80,90,100]
arr = np.array(l)
print(arr[1:4]) # it's means that its start from 1 no index and end before 4 no index
print(arr[5:]) # it's mean that its start form 5 no index and end to last
print(arr[:5]) # it's mean that is's start form begain and end before the 5 no index


# In[23]:


# Negative Slicing

n = [1,2,3,4,5,6,7,8,9,10]
arr = np.array(n)
print(arr[-3:-1]) # start : end
print(arr[1:5:2]) #start : end : step
print(arr[-5:-1:2]) # Negative Scling


# In[26]:


# Slicing 2-D array

arr = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(arr)
print(arr[1, 1:4])
print(arr[0:2,3]) # row, column
print(arr[0:2, 1:4])


# In[27]:


arr = np.array([1,2,3,4])
print(arr)
print(type(arr))
print(arr.dtype) # define for data type


# In[28]:


arr = np.array([1,2,3,4], dtype='i8') # change to: "dtype=i8"
print(arr)
print(arr.dtype)


# In[41]:


# Using ob.astype()

arr = np.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6])
#newarr = arr.astype(bool) # cheak that all the elements are bool or not
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)


# In[42]:


# Numpy array shape
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr.shape)


# In[5]:


# Numpy array Reshaping

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

newarr = arr.reshape(4, 3) # No of Rows : No of Column
print(newarr)
print("")
newarr2 = arr.reshape(2, 2, 3) # dimantion : row : column
print(newarr2)


# In[6]:


# Flattening the array

arr = np.array([[1,2,3],[4,5,6]])
newarr = arr.reshape(-1)
print(newarr)


# In[13]:


# Numpy.arrange

print(np.arange(4).reshape(2, 2)) # arrange(4) means the array start from 0 and before 4
print(" ")
print(np.arange(4,10).reshape(3,2), "\n") # arrange(4,10) means that start 4 and end before 10
print("")
print(np.arange(4, 15, 3), "\n") # arrange(4,15,3)--start:end:step


# In[ ]:




