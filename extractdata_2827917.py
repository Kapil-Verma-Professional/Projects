#!/usr/bin/env python
# coding: utf-8

# In[84]:


import sqlite3
import mysql.connector
import json
import collections
import pandas as pd


# In[67]:


conn = sqlite3.connect('cma-artworks.db')
cursor = conn.cursor()


# In[97]:


cursor.execute("SELECT * FROM EMPLOYEE")
rows = cursor.fetchall()
# Convert query to objects of key-value pairs
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d["FIST_NAME"] = row[0]
    d["LAST_NAME"] = row[1]
    d["AGE"] = row[2]
    d["SEX"] = row[3]
    d["INCOME"] = row[4]
    objects_list.append(d)
j = json.dumps(objects_list, indent=0)
with open("emp.txt", "w") as f:
    f.write(j)
#conn.close()
print(j)


# In[96]:


cursor.execute("SELECT * FROM department")
rows = cursor.fetchall()
# Convert query to objects of key-value pairs
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d["id"] = row[0]
    d["NAME"] = row[1]
    objects_list.append(d)
j = json.dumps(objects_list, indent=0)
with open("department.txt", "w") as f:
    f.write(j)
#conn.close()
print(j)


# In[95]:


cursor.execute("SELECT * FROM creator")
rows = cursor.fetchall()
# Convert query to objects of key-value pairs
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d["id"] = row[0]
    d["role"] = row[1]
    d["description"] = row[2]
    objects_list.append(d)
j = json.dumps(objects_list, indent=0)
with open("creator.txt", "w") as f:
    f.write(j)
#conn.close()
print(j)


# In[94]:


cursor.execute("SELECT * FROM artwork")
rows = cursor.fetchall()
# Convert query to objects of key-value pairs
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d["id"] = row[0]
    d["accession_number"] = row[1]
    d["title"] = row[2]
    d["tombstone"] = row[3]
    objects_list.append(d)
j = json.dumps(objects_list, indent=0)
with open("artwork.txt", "w") as f:
    f.write(j)
#conn.close()
print(j)


# In[93]:


cursor.execute("SELECT * FROM artwork__creator")
rows = cursor.fetchall()
# Convert query to objects of key-value pairs
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d["artwork_id"] = row[0]
    d["creator_id"] = row[1]
    objects_list.append(d)
j = json.dumps(objects_list, indent=0)
with open("art_creator_.txt", "w") as f:
    f.write(j)
#conn.close()
print(j)


# In[87]:


cursor.execute("SELECT * FROM artwork__department")
rows = cursor.fetchall()
# Convert query to objects of key-value pairs
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d["artwork_id"] = row[0]
    d["department_id"] = row[1]
    objects_list.append(d)
j = json.dumps(objects_list, indent=0)
#conn.close()
with open("art_dept_.txt", "w") as f:
    f.write(j)
print(j)


# In[99]:


# Python program to
# demonstrate merging
# of two files
  
data = data2 = ""
  
# Reading data from file1
with open('emp.txt') as fp:
    data = fp.read()
with open('department.txt') as fp:
    data2 = fp.read()
# To add the data of file2
# from next line
data += "\n"
data += data2
  
with open ('file3.txt', 'w') as fp:
    fp.write(data)


# In[100]:


data = data2 = ""
  
# Reading data from file1
with open('creator.txt') as fp:
    data = fp.read()
with open('artwork.txt') as fp:
    data2 = fp.read()
# To add the data of file2
# from next line
data += "\n"
data += data2
  
with open ('file4.txt', 'w') as fp:
    fp.write(data)


# In[101]:


data = data2 = ""
  
# Reading data from file1
with open('art_creator_.txt') as fp:
    data = fp.read()
with open('art_dept_.txt') as fp:
    data2 = fp.read()
# To add the data of file2
# from next line
data += "\n"
data += data2
  
with open ('file5.txt', 'w') as fp:
    fp.write(data)


# In[107]:


data = data2 = ""
# Reading data from file1
with open('file3.txt') as fp:
    data = fp.read()
with open('file4.txt') as fp:
    data2 = fp.read()
# To add the data of file2
# from next line
data += "\n"
data += data2
  
with open ('file6.txt', 'w') as fp:
    fp.write(data)


# In[108]:


data = data2 = ""
# Reading data from file1
with open('file6.txt') as fp:
    data = fp.read()
with open('file5.txt') as fp:
    data2 = fp.read()
# To add the data of file2
# from next line
data += "\n"
data += data2
  
with open ('artworks.txt', 'w') as fp:
    fp.write(data)


# In[ ]:




