#!/usr/bin/env python
# coding: utf-8

# Example of performing linear least squares fitting

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np


# Generating random data

# In[12]:



#set random number seed, seeding random number generator
np.random.seed(119)
npoints = 50
x=np.linspace(0,10.,npoints)
#set slope, intercept, and scatter rms, these are underlying trends
m = 2.0
b = 1.0
sigma = 2.0

#generate y points
y = m*x + b + np.random.normal(scale=sigma, size=npoints)
y_err = np.full(npoints, sigma)


# To make sure line is accurate, can simulate data, make fake data

# Let's plot data

# In[4]:


f = plt.figure(figsize=(7,7))
plt.errorbar(x,y, sigma, fmt='o')
plt.xlabel('x')
plt.ylabel('y')


# Method #1, polyfit

# In[15]:


m_fit, b_fit = np.poly1d(np.polyfit(x, y, 1, w=1./y_err)) #weight with uncertainties, y_err not yet defined
print(m_fit, b_fit)

y_fit = m_fit*x + b_fit

f = plt.figure(figsize=(7,7))
plt.errorbar(x,y, yerr=y_err, fmt='o', label ='data')
plt.plot(x,y_fit,label='fit')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=2,frameon=False)


# In[ ]:




