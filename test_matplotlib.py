#!/usr/bin/env python
# coding: utf-8

# In[ ]:



get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1)  #0-5 in 0.1 increments
y = np.sin(x)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('sin(x)')
#plt.show()
plt.savefig('sinx.png', bbox_inches="tight", dpi=600)


# #making multiple panels

# In[14]:


#making multiple panels
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0, 2*np.pi, 100)
print(x[-1], 2*np.pi)

y = np.sin(x)
z = np.cos(x)
w = np.sin(4*x)
v = np.cos(4*x)


# making multi panel figues, make two-panel plot side-by-side

# In[12]:


#call subplots to generate multi panel figures, 1 row 2 columns
f, axarr = plt.subplots(1,2)
#treat axarr as an array from left to right

#first panel
axarr[0].plot(x,y)
axarr[0].set_xlabel('x')
axarr[0].set_ylabel('sin(x)')
axarr[0].set_title(r'$\sin(x)$')

#second panel
axarr[1].plot(x,z)
axarr[1].set_xlabel('x')
axarr[1].set_ylabel('cos(x)')
axarr[1].set_title(r'$\cos(x)$')
#add more spaces
f.subplots_adjust(wspace=0.4)
#fixing axis ratio, below are two ways
axarr[0].set_aspect('equal')
axarr[1].set_aspect(np.pi)


# Keep square figure, merge into one, remove titles and add legends

# In[17]:


fig =plt.figure(figsize=(6,6))

plt.plot(x, y, label= r'$y= \sin(x)$')
plt.plot(x, z, label= r'$y= \cos(x)$')
plt.plot(x, w, label= r'$y = \sin(4x)$')
plt.plot(x, v, label = r'$y= \cos(4x)$')

plt.xlabel(r'$x$')
plt.ylabel(r'$y(x)$')
plt.xlim([0, 2*np.pi])
plt.ylim([-1.2, 1.2])
plt.legend(loc=1, framealpha=0.95)

#fix the axis ratio
plt.gca().set_aspect(np.pi/1.2) #get current axis


# 

# In[ ]:




