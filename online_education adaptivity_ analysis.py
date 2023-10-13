#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install numpy')


# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv("/Users/feliciasmac/Downloads/students_adaptability_level_online_education.csv")


# In[3]:


#getting familiar with my dataset- i will convert most datatype to counts to do my analysis
df.info() #this means that every student was interviewed


# In[6]:


df.describe()


# In[8]:


df.sort_values(by="Financial Condition")


# In[15]:


sns.countplot(x='Financial Condition', data=df) #majority of the students are in the Mid-class


# In[30]:


df.sort_values(by="Load-shedding" and "Class Duration").head(5)


# In[22]:


df.isnull().sum() #there are no missing values 


# In[33]:


sns.countplot(x="Network Type",data=df) #network type being used by most students #4G is mostly used


# In[42]:


category_counts = df['Load-shedding'].value_counts() #converting load shedding to count /countable
df


# In[47]:


category_counts.plot.pie(autopct='%1.1f%%', startangle=90)
plt.axis('equal')  
plt.title('Students with high vs Low Load shedding Experience')
plt.show()
#does this mean that majority of students do not experience loadshedding?


# In[64]:


IT_counts = df['IT Student'].value_counts()
df


# In[67]:


IT_counts.plot.pie(autopct='%1.1f%%', startangle=90) #majority of the students are not IT students


# In[68]:


Gender_counts = df['Gender'].value_counts() #converting gender to counts for visualization purposes
df


# In[69]:


Gender_counts.plot.pie(autopct='%1.1f%%', startangle=90) #The msot gender presented?more boys than girls however not a significant difference 10%


# In[70]:


sns.countplot(x='Age', data=df) #majority of the students represented in this dataset are between this age


# In[71]:


sns.countplot(x='Institution Type', data=df) #majority of students are from Non Government Institutions


# In[72]:





# In[73]:


Education_counts = df['Education Level'].value_counts()
df


# In[74]:


Education_counts.plot.pie(autopct='%1.1f%%', startangle=90) #majority are in school(kind,pri,sec)


# In[79]:


df.sort_values(by="IT Student")


# In[91]:


sns.countplot(x='Internet Type', data=df) #majority of students use mobile data


# In[93]:


sns.countplot(x='Adaptivity Level', data=df) #this is the adaptivity level of the students- alot of work still needs to be done to get high adaptivity 


# In[ ]:




