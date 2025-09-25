#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
data={
    "ID":[1,2,3,4,5],"Name":["Kubra","Barshanaa","Afreen","Sana","Nenu"],"Age":[21,24,25,26,28],
    "Department":["IT","EEE","MECH","ECE","CSE"],
    "Marks":[93,93,83,82,81]
}
df=pd.DataFrame(data)
print(df)
df.to_csv("kubra's Mini Project 2.csv",index=False)
print("Data saved to sample_data.csv")


# In[ ]:





# In[ ]:




