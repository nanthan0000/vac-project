#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install bs4


# In[2]:


pip install requests


# In[3]:


from bs4 import BeautifulSoup


# In[4]:


import requests


# In[5]:


pip install pandas


# In[6]:


url = "https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=61d24dd4-26b3-4d10-a605-f1eac9d72e08"


# In[7]:


allow = requests.get(url)


# In[8]:


print(allow)


# In[9]:


soup = BeautifulSoup(allow.text)


# In[10]:


product_name = soup.select("._4rR01T")


# In[11]:


product_name


# In[12]:


product_link=[]


# In[13]:


product_title=[]


# In[14]:


for item in product_name:
    product_title.append(item.text)
    link = "https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=61d24dd4-26b3-4d10-a605-f1eac9d72e08"
    product_link.append(link)


# In[15]:


product_link


# In[16]:


product_rate = soup.select("._1_WHN1")


# In[17]:


product_rate


# In[18]:


product_title


# In[19]:


product_cost = []
product_junk = []


# In[20]:


for item in product_rate:
    product_cost.append(item.text)
    junk = "https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=61d24dd4-26b3-4d10-a605-f1eac9d72e08"
    product_junk.append(junk)


# In[21]:


product_cost


# In[24]:


import pandas as pd


# In[25]:


product = pd.DataFrame(product_name,columns=["product_name"])


# In[26]:


product["cost"] = product_cost


# In[27]:


product.to_csv("product.csv")


# In[28]:


product


# In[ ]:




