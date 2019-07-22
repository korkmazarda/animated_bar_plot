#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import necessary libraries
import pandas as pd


# In[3]:


# Read the Spotify dataset
df = pd.read_csv('spotify_dataset.csv')


# In[4]:


df.head()


# In[5]:


# Take a look at the region labels
df["Region"].unique()


# In[6]:


# Create a dictionary mapping for the real region values (https://www.spotify.com/us/select-your-country/)
region_dic = {'ar':'Argentina', 'at':'Austria', 'au':'Australia', 'be':'Belgium', 'bo':'Bolivia', 'br':'Brazil', 
       'ca':'Canada', 'ch':'Switzerland', 'cl':'Chile', 'co':'Columbia', 'cr':'CostaRica', 'cz':'CzechRepublic', 
       'de':'Germany', 'dk':'Denmark', 'do':'DominicanRepublic', 'ec':'Ecuador', 'ee':'Estonia', 'es':'Spain', 
       'fi':'Finland', 'fr':'France', 'gb':'UnitedKingdom', 'global':'Global', 'gr':'Greece', 'gt':'Guatemala', 
       'hk':'HongKong', 'hn':'Honduras', 'hu':'Hungary', 'id':'Indonesia', 'ie':'Ireland', 'is':'Iceland', 
       'it':'Italy', 'jp':'Japan', 'lt':'Lithuania', 'lu':'Luxemborg', 'lv':'Latvia', 'mx':'Mexico', 
       'my':'Malaysia', 'nl':'Netherlands', 'no':'Norway', 'nz':'NewZealand', 'pa':'Panama', 'pe':'Peru', 
       'ph':'Philippines', 'pl':'Poland', 'pt':'Portugal', 'py':'Paraguay', 'se':'Sweden', 'sg':'Singapore', 
       'sk':'Slovakia', 'sv':'ElSalvador', 'tr':'Turkey', 'tw':'Taiwan', 'us':'USA', 'uy':'Uruguay'}


# In[7]:


# Replace with the true Region names
df = df.replace({"Region":region_dic})


# In[8]:


# Replace the Date type for ease of use and creating extra columns
df.Date = pd.to_datetime(df["Date"])


# In[9]:


# Create year, month, day and day of the week columns
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Day_of_week'] = df['Date'].dt.dayofweek


# In[12]:


# Combine Track name and Artist for ease of use
df['Title'] = df['Artist'] +' - '+ df['Track Name']


# In[13]:


df.head()


# In[16]:


df_usa_1701 = df[(df.Region == "USA") & (df.Year == 2017) & (df.Month.isin([1]))].groupby(["Title"],as_index=False).agg({"Streams": "sum"}).sort_values(["Streams"], ascending=[False]).head(10).reset_index(drop=True)
df_usa_1701.index = df_usa_1701.index + 1
df_usa_1701["YearMonth"] = 201701
df_usa_1701 = df_usa_1701.reset_index()

df_usa_1702 = df[(df.Region == "USA") & (df.Year == 2017) & (df.Month.isin([1,2]))].groupby(["Title"],as_index=False).agg({"Streams": "sum"}).sort_values(["Streams"], ascending=[False]).head(10).reset_index(drop=True)
df_usa_1702.index = df_usa_1702.index + 1
df_usa_1702["YearMonth"] = 201702
df_usa_1702 = df_usa_1702.reset_index()

df_usa_1703 = df[(df.Region == "USA") & (df.Year == 2017) & (df.Month.isin([1,2,3]))].groupby(["Title"],as_index=False).agg({"Streams": "sum"}).sort_values(["Streams"], ascending=[False]).head(10).reset_index(drop=True)
df_usa_1703.index = df_usa_1703.index + 1
df_usa_1703["YearMonth"] = 201703
df_usa_1703 = df_usa_1703.reset_index()

df_usa_1704 = df[(df.Region == "USA") & (df.Year == 2017) & (df.Month.isin([1,2,3,4]))].groupby(["Title"],as_index=False).agg({"Streams": "sum"}).sort_values(["Streams"], ascending=[False]).head(10).reset_index(drop=True)
df_usa_1704.index = df_usa_1704.index + 1
df_usa_1704["YearMonth"] = 201704
df_usa_1704 = df_usa_1704.reset_index()

df_usa_1705 = df[(df.Region == "USA") & (df.Year == 2017) & (df.Month.isin([1,2,3,4,5]))].groupby(["Title"],as_index=False).agg({"Streams": "sum"}).sort_values(["Streams"], ascending=[False]).head(10).reset_index(drop=True)
df_usa_1705.index = df_usa_1705.index + 1
df_usa_1705["YearMonth"] = 201705
df_usa_1705 = df_usa_1705.reset_index()

df_usa_1706 = df[(df.Region == "USA") & (df.Year == 2017) & (df.Month.isin([1,2,3,4,5,6]))].groupby(["Title"],as_index=False).agg({"Streams": "sum"}).sort_values(["Streams"], ascending=[False]).head(10).reset_index(drop=True)
df_usa_1706.index = df_usa_1706.index + 1
df_usa_1706["YearMonth"] = 201706
df_usa_1706 = df_usa_1706.reset_index()

df_usa_1707 = df[(df.Region == "USA") & (df.Year == 2017) & (df.Month.isin([1,2,3,4,5,6,7]))].groupby(["Title"],as_index=False).agg({"Streams": "sum"}).sort_values(["Streams"], ascending=[False]).head(10).reset_index(drop=True)
df_usa_1707.index = df_usa_1707.index + 1
df_usa_1707["YearMonth"] = 201707
df_usa_1707 = df_usa_1707.reset_index()

df_usa_1708 = df[(df.Region == "USA") & (df.Year == 2017) & (df.Month.isin([1,2,3,4,5,6,7,8]))].groupby(["Title"],as_index=False).agg({"Streams": "sum"}).sort_values(["Streams"], ascending=[False]).head(10).reset_index(drop=True)
df_usa_1708.index = df_usa_1708.index + 1
df_usa_1708["YearMonth"] = 201708
df_usa_1708 = df_usa_1708.reset_index()

df_usa_1709 = df[(df.Region == "USA") & (df.Year == 2017) & (df.Month.isin([1,2,3,4,5,6,7,8,9]))].groupby(["Title"],as_index=False).agg({"Streams": "sum"}).sort_values(["Streams"], ascending=[False]).head(10).reset_index(drop=True)
df_usa_1709.index = df_usa_1709.index + 1
df_usa_1709["YearMonth"] = 201709
df_usa_1709 = df_usa_1709.reset_index()

df_usa_1710 = df[(df.Region == "USA") & (df.Year == 2017) & (df.Month.isin([1,2,3,4,5,6,7,8,9,10]))].groupby(["Title"],as_index=False).agg({"Streams": "sum"}).sort_values(["Streams"], ascending=[False]).head(10).reset_index(drop=True)
df_usa_1710.index = df_usa_1710.index + 1
df_usa_1710["YearMonth"] = 201710
df_usa_1710 = df_usa_1710.reset_index()

df_usa_1711 = df[(df.Region == "USA") & (df.Year == 2017) & (df.Month.isin([1,2,3,4,5,6,7,8,9,10,11]))].groupby(["Title"],as_index=False).agg({"Streams": "sum"}).sort_values(["Streams"], ascending=[False]).head(10).reset_index(drop=True)
df_usa_1711.index = df_usa_1711.index + 1
df_usa_1711["YearMonth"] = 201711
df_usa_1711 = df_usa_1711.reset_index()

df_usa_1712 = df[(df.Region == "USA") & (df.Year == 2017) & (df.Month.isin([1,2,3,4,5,6,7,8,9,10,11,12]))].groupby(["Title"],as_index=False).agg({"Streams": "sum"}).sort_values(["Streams"], ascending=[False]).head(10).reset_index(drop=True)
df_usa_1712.index = df_usa_1712.index + 1
df_usa_1712["YearMonth"] = 201712
df_usa_1712 = df_usa_1712.reset_index()

df_usa_1801 = df[(df.Region == "USA") & (df.Year.isin([2017,2018])) & (df.Month.isin([1,2,3,4,5,6,7,8,9,10,11,12]))].groupby(["Title"],as_index=False).agg({"Streams": "sum"}).sort_values(["Streams"], ascending=[False]).head(10).reset_index(drop=True)
df_usa_1801.index = df_usa_1801.index + 1
df_usa_1801["YearMonth"] = 201801
df_usa_1801 = df_usa_1801.reset_index()


# In[17]:


df_usa_1711


# In[18]:


frames = [df_usa_1701, df_usa_1702, df_usa_1703, df_usa_1704, df_usa_1705, df_usa_1706, df_usa_1707, df_usa_1708, df_usa_1709, df_usa_1710, df_usa_1711, df_usa_1712, df_usa_1801]
df_usa_merged = pd.concat(frames)


# In[19]:


df_usa_merged.to_csv('df_usa_merged.csv')

