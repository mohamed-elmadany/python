#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[1]:


import calc
while 1:
    inp1=input("please enter the operation and 2 numbers comma seperated\n")
    op,x,y=inp1.split(',')
    if op=="add":
        result=calc.add(int(x),int(y))
    elif op=="sub":
        result=calc.sub(int(x),int(y))
    elif op=="div":
        result=calc.div(int(x),int(y))
    elif op=="mult":
        result=calc.mult(int(x),int(y))
    else: 
        print("please enter a valid operation")
    print("result=",result)
    inp2=input("do you want to make another operation yes or no\n")
    if inp2=="yes":
        continue
    else:
        break


# In[ ]:




