#!/usr/bin/env python
# coding: utf-8

# In[1]:


L = "listen"
L1 = "silent"

print(sorted(L))
print(sorted(L1))

if sorted(L)==sorted(L1):
    print("Anagrams")
else:
    print("This is No Anagram")


# In[2]:


L = "listen"
L1 = "silent"
if len(L)==len(L1):
    L_sorted=''.join(sorted(L))
    L1_sorted=''.join(sorted(L1))
    if sorted(L)==sorted(L1):
        print("Anagram")
    else:
        print("not")
else:
    print("n")


# In[ ]:




