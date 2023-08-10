#!/usr/bin/env python
# coding: utf-8

# In[6]:


import sqlite3
import pandas as pd


# In[7]:


pip install PyMySQL


# In[21]:


pip install mysql-connector 


# In[22]:


#libraries installation before connection is required
from pymysql import connect
import mysql.connector


# In[40]:


##upload the database cma-artworks.db file on the ide where you want to run the python script
conn = sqlite3.connect('cma-artworks.db')


# In[55]:


#connecting to the cursor to excetue and fetch tha tables and columns from teh database
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())


# ### The database contains 6 files 
# **('artwork__department',), ('artwork',), ('creator',), ('department',), ('artwork__creator',), ('EMPLOYEE',)**

# In[47]:


df1 = pd.read_sql_query("SELECT * from EMPLOYEE", conn)
df1


# In[48]:


df2 = pd.read_sql_query("SELECT * from artwork__creator", conn)
df2


# In[49]:


df3 = pd.read_sql_query("SELECT * from department", conn)
df3


# In[51]:


df4= pd.read_sql_query("SELECT * from creator", conn)
df4


# In[52]:


df5 = pd.read_sql_query("SELECT * from artwork", conn)
df5


# In[54]:


df6 = pd.read_sql_query("SELECT * from artwork__department", conn)
df6

