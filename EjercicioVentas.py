#!/usr/bin/env python
# coding: utf-8

# In[11]:


get_ipython().run_line_magic('config', 'Completer.use_jedi = False')
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:75% !important; }</style>"))


# In[8]:


import pandas as pd


# In[19]:


from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches


# In[16]:


lifestore_products_df = pd.DataFrame(columns=['id_product', 'name', 'price','category','stock'])
for i in range(len(lifestore_products)):
    lifestore_products_df.loc[i] = lifestore_products[i]
    
    
lifestore_products_df


# In[23]:


#id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false
lifestore_sales_df = pd.DataFrame(columns=['id_sale', 'id_product', 'score','date','refund'])
for i in range(len(lifestore_sales)):
    lifestore_sales_df.loc[i] = lifestore_sales[i]

lifestore_sales_df


# In[24]:


#lifestore_searches = [id_search, id product]
lifestore_searches_df = pd.DataFrame(columns= ['id_search', 'id product'])
for i in range(len(lifestore_searches)):
    lifestore_searches_df.loc[i] = lifestore_searches[i]

lifestore_searches_df


# In[46]:


#lifestore_sales_df.loc[lifestore_sales_df.refund == 0]

ventas_validas = pd.merge(lifestore_products_df, lifestore_sales_df.loc[lifestore_sales_df.refund == 0], on='id_product' )#.fillna(0)
top_ventas = ventas_validas[['name','id_sale']].groupby(['name']).count().reset_index().rename({'id_sale':'sales_count'}, axis='columns')
top_ventas.sort_values(by='sales_count',ascending=False, inplace=True)
top_ventas.tail(10)


# In[47]:


ventas_validas

