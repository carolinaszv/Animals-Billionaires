#!/usr/bin/env python
# coding: utf-8

# # Homework 5, Part 2: Answer questions with pandas
# 
# **Use the Excel file to answer the following questions.** This is a little more typical of what your data exploration will look like with pandas.

# ## 0) Setup
# 
# Import pandas **with the correct name** .

# In[1]:


import pandas as pd


# ## 1) Reading in an Excel file
# 
# Use pandas to read in the `richpeople.xlsx` Excel file, saving it as a variable with the name we'll always use for a dataframe.
# 
# > **TIP:** You will use `read_excel` instead of `read_csv`. Trying `read_excel` the first time will probably not work, you'll get an error message. Be sure to read the error carefully: *you probably need to install a new library before it will work, and the error tells you what the library is named*.

# In[2]:


df = pd.read_excel('richpeople.xlsx')
df


# ## 2) Checking your data
# 
# Display the number of rows and columns in your data. Also display the names and data types of each column.

# In[3]:


df.shape


# In[4]:


df.dtypes


# In[ ]:





# ## 3) Who are the top 10 richest billionaires? Use the `networthusbillion` column.

# In[5]:


df.sort_values(by='networthusbillion', ascending=False).name.head(10)


# ## 4) How many male billionaires are there compared to the number of female billionares? What percent is that? Do they have a different average wealth?
# 
# > **TIP:** The last part uses `groupby`, but the count/percent part does not.
# > **TIP:** When I say "average," you can pick what kind of average you use.

# In[6]:


df.value_counts('gender')#.plot(kind='barh',title='Male vs Female Billionaires')


# In[7]:


round(df.value_counts('gender')/len(df)*100,1)


# In[8]:


df.groupby('gender').networthusbillion.median()


# ## 5) What is the most common source/type of wealth? Is it different between males and females?
# 
# > **TIP:** You know how to `groupby` and you know how to count how many times a value is in a column. Can you put them together???
# > **TIP:** Use percentages for this, it makes it a lot more readable.

# In[9]:


df.groupby('typeofwealth').name.count().sort_values(ascending=False)[:1]


# In[10]:


#df_fem = df[df['gender'] == 'female']
round((df.groupby(['gender','typeofwealth']).name.count()/len(df))*100,2)


# ## 6) What companies have the most billionaires? Graph the top 5 as a horizontal bar graph.
# 
# > **TIP:** First find the answer to the question, then just try to throw `.plot()` on the end
# >
# > **TIP:** You can use `.head()` on *anything*, not just your basic `df`
# >
# > **TIP:** You might feel like you should use `groupby`, but don't! There's an easier way to count.
# >
# > **TIP:** Make the largest bar be at the top of the graph
# >
# > **TIP:** If your chart seems... weird, think about where in the process you're sorting vs using `head`

# In[11]:


df.value_counts('company')[:5].sort_values(ascending=True).plot(kind='barh')


# ## 7) How much money do these billionaires have in total?

# In[12]:


df.value_counts('networthusbillion').sum()


# ## 8) What are the top 10 countries with the most money held by billionaires?
# 
# I am **not** asking which country has the most billionaires - this is **total amount of money per country.**
# 
# > **TIP:** Think about it in steps - "I want them organized by country," "I want their net worth," "I want to add it all up," and "I want 10 of them." Just chain it all together.

# In[13]:


df.groupby(by='citizenship').networthusbillion.sum().sort_values(ascending=False)[:10]


# ## 9) How old is an average billionaire? How old are self-made billionaires  vs. non self-made billionaires? 

# In[19]:


round(df.age.mean())


# In[20]:


round(df.groupby(by='selfmade').age.mean())


# ## 10) Who are the youngest billionaires? Who are the oldest? Make a graph of the distribution of ages.
# 
# > **TIP:** You use `.plot()` to graph values in a column independently, but `.hist()` to draw a [histogram](https://www.mathsisfun.com/data/histograms.html) of the distribution of their values

# In[52]:


df.sort_values(by='age', ascending=True).name[:10]


# In[53]:


df.sort_values(by='age', ascending=False).name[:10]


# In[56]:


df.age.hist()


# ## 11) Make a scatterplot of net worth compared to age

# In[74]:


df.plot.scatter(x='age', y='networthusbillion')
#can add c=for color


# ## 13) Make a bar graph of the wealth of the top 10 richest billionaires
# 
# > **TIP:** When you make your plot, you'll need to set the `x` and `y` or else your chart will look _crazy_
# >
# > **TIP:** x and y might be the opposite of what you expect them to be

# In[145]:


df.groupby(by='name').networthusbillion.max().sort_values(ascending=False)[:10].sort_values().plot(kind='barh',title='Wealth of top 10 richest billionaires', x='networthusbillion',y='name')
#df.networthusbillion.sort_values(ascending=False)[:10].sort_values().plot(kind='barh', x='networthusbillion',y='name')
#why does the above not work?


# In[ ]:




