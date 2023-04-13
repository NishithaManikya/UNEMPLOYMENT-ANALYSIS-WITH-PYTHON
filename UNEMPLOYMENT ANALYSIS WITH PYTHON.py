#!/usr/bin/env python
# coding: utf-8

# In[1]:


from requests import get
from warnings import warn
from time import sleep
from random import randint
import numpy as np, pandas as pd
import seaborn as sns
import re
from matplotlib import pyplot as plt
from warnings import filterwarnings


# In[2]:


## Import the data
df=pd.read_csv("Unemployment_Rate_upto_11_2020.csv")
df


# In[3]:


#change coloum name for understanding
df.columns= ["States","Date","Frequency",
               "Estimated Unemployment Rate",
               "Estimated Employed",
               "Estimated Labour Participation Rate",
               "Region","longitude","latitude"]


# In[4]:


## Describe the data
df.describe()


# In[5]:


##Head is used to find first 5 data
df.head()


# In[6]:


#Tail is used to find last five data
df.tail()


# In[7]:


#Check if this dataset contains missing values or not:
print(df.isnull().sum())


# ## Data Visualization

# In[21]:


sns.heatmap(df.corr(),annot=True);##heatmap


# In[22]:


df.groupby('Region').agg({'Estimated Unemployment Rate':['min','max','mean']})##groupby


# In[8]:


#visualize the data to analyze the unemployment rate. estimated number of employees according to different regions of India:
df.columns= ["States","Date","Frequency",
               "Estimated Unemployment Rate","Estimated Employed",
               "Estimated Labour Participation Rate","Region",
               "longitude","latitude"]
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Unemployment Rate", hue="Region", data=df)
plt.show()


# By the above hist graph we can understand that unemployment rate is higher in south and north

# In[9]:


#visualize the data to analyze the unemployment rate. estimated number of employees according to different regions of India:
df.columns= ["States","Date","Frequency",
               "Estimated Unemployment Rate","Estimated Employed",
               "Estimated Labour Participation Rate","Region",
               "longitude","latitude"]
plt.title("Indian Employment")
sns.histplot(x="Estimated Employed", hue="Region", data=df)
plt.show()
     


# In[10]:


sns.violinplot(df['Region'],df['Estimated Unemployment Rate'])


# In[11]:


sns.pairplot(df)


# In[15]:


pd.crosstab(df['Estimated Unemployment Rate'],df['Region']).sum().plot.bar()


# In[13]:


# To find the outliers we use box plot
sns.boxplot(df['Estimated Unemployment Rate'],df['Region'])


# In[16]:


sns.scatterplot(data=df,y='Estimated Unemployment Rate',x='Region',color='red')
plt.xticks(rotation =90)
plt.show()


# In[17]:


sns.jointplot(data = df, x='Region',y='Estimated Unemployment Rate')


# In[18]:


sns.distplot(df['Estimated Unemployment Rate']);


# In[20]:


df.groupby(['Region']).sum().plot(kind='pie', y='Estimated Unemployment Rate')


# In[28]:


df[['latitude','Estimated Unemployment Rate']].groupby('latitude').count().plot(kind='bar', title='UNEMPLOYMENT ANALYSIS ')
plt.ylabel('Estimated Unemployment Rate')
plt.xlabel('latitude')


# ## Conclusion

# By the above analysis we can conclude that there is large number of unemployment in North and South region
