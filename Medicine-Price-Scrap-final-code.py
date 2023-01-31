#!/usr/bin/env python
# coding: utf-8

# #### Defined function for website Aroggo Scraping

# In[1]:


def scrap(aroggo_url):
    
    #print('Function initialed')
    # Medicine name, Price name
    import requests
    from bs4 import BeautifulSoup
    page = requests.get(url=aroggo_url) #to get into the url
    soup = BeautifulSoup(page.content,'html.parser') #get html code in a good manner
    price_element = soup.find(class_ = 'jss9') # get price element
    price = price_element.get_text() # Removing html tags
    meidicine_price  = price.strip('Best Price') 

    medicine_name=soup.find(class_ = 'MuiTypography-root jss3 MuiTypography-h1').text  #only to use text
    #Cleaning Price
    meidicine_price = float(meidicine_price[1:])   # manipulate string as array

    return {
        'medicine_name':medicine_name,
        'meidicine_price':meidicine_price,
    }


# #### Defined Function for Output  Visual Presentation 

# In[2]:


def myPlot(name,price):
   
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax=fig.add_axes([1,1,1,1])
    x=name
    y=price
    plt.xlabel("Medicine Name,Power & Company",color="red",size=11)
    plt.ylabel("Medicine Price",color="red",size=11)
    plt.title("Medicine Price Comparison Of Different Companies",color="black",size=16)
    plt.xticks(fontsize=5.4)
    c=["m","r","y","g","c"]
    ax.bar(x,y,width=0.5,color=c,edgecolor="k",linewidth=2)
    plt.show()


# #### All Links for Scraping the Required Medicines

# In[3]:


fever={
    'cause':'fever',
    'beximco':'https://www.arogga.com/brand/12480/napa-rapid-tablet-500m',
    'Globe':'https://www.arogga.com/brand/9816/kapron-tablet-500mg',
    'aristopharma-antibiotic':'https://www.arogga.com/brand/20595/xpa-tablet-500mg',#antibiotic
    'Delta':'https://www.arogga.com/brand/25129/dfx-tablet-500mg',
    'ACME':'https://www.arogga.com/brand/7311/fast-tablet-500mg'
    }
sinusitis={
    'cause':'sinusitis',
    'Cosmo':'https://www.arogga.com/brand/25576/amoxic-capsule-250mg',
    'Pacific':'https://www.arogga.com/brand/24398/amocin-capsule-250mg',
    'Delta-antibiotic':'https://www.arogga.com/brand/25129/dfx-tablet-500mg', #antibiotic
    'Incepta':'https://www.arogga.com/brand/6287/efdinir-capsule-300mg',
    'Square':'https://www.arogga.com/brand/29901/livolite-capsule-200mg'
   
    }
toncilities={
    'cause':'toncilities',
    'Pharmasia-antibiotic':'https://www.arogga.com/brand/2029/azexia-tablet-500mg', #antibiotic 
    'Gonoshasthaya':'https://www.arogga.com/brand/8367/g-amoxicillin-capsule-250mg',
    'Albion':'https://www.arogga.com/brand/3712/cefuroxime-tablet-125mg',
    'Renata':'https://www.arogga.com/brand/8309/furocef-tablet-125mg',
    'Eskayef':'https://www.arogga.com/brand/10013/kilmax-tablet-125mg'
    
    }
pain={
    'cause':'pain',
    'beximco':'https://www.arogga.com/brand/12480/napa-rapid-tablet-500m',
    'Apollo':'https://www.arogga.com/brand/15516/promel-tablet-500mg',
    'aristopharma-antibiotic':'https://www.arogga.com/brand/20595/xpa-tablet-500mg',#antibiotic
    'Biopharma':'https://www.arogga.com/brand/25559/aceta-tablet-500mg',
    'ACME':'https://www.arogga.com/brand/7311/fast-tablet-500mg'
     }
burn={
    'cause':'burn',
    'Square ':'https://www.arogga.com/brand/23502/burna-cream-cream-1',
    'Kumudini ':'https://www.arogga.com/brand/2912/burnaid-cream-1',
    'Opsonin ':'https://www.arogga.com/brand/22657/neozine-cream-1',
    'Sibalyn':'https://www.arogga.com/brand/25365/sibalyn-cream-1',
    'Healthcare':'https://www.arogga.com/brand/17511/silverax-cream-1'
    }
acidity={
    'cause':'acidity',
    'Renata-antibiotic':'https://www.arogga.com/brand/11272/maxpro-hp-kit-20mg500mg500mg ',#antibiotic
    'Ziska':'https://www.arogga.com/brand/6883/esoprol-20-capsule-20mg',
    'Square':'https://www.arogga.com/brand/17160/seclo-20-capsule-20mg',
    'Pharmasia':'https://www.arogga.com/brand/20388/xelpro-capsule-20mg',
    'Orion':'https://www.arogga.com/brand/7166/exor-20-capsule-20mg'
    }
cut={
    'cause':'cut',
    'ACME':'https://www.arogga.com/brand/12783/neotracin-ointment-500iu5mggm',
    'Opsonin':'https://www.arogga.com/brand/24987/neocin-ointment-500iu5mggm',
    'Gaco':'https://www.arogga.com/brand/2177/b-mycin-ointment-500iu5mggm',
    'Incepta':'https://www.arogga.com/brand/23468/nebazin-ointment-500iu5mggm',
    'Pharmadesh':'https://www.arogga.com/brand/23222/nebacin-ointment-500iu5mggm'
    }

all_links=[fever,sinusitis,toncilities,pain,burn,acidity,cut]


# ### Creating Pandas data frame, scraping, storing and saving

# ####Creating dataframe using panda

# In[4]:


import pandas as pd
columns=['Cause','Medicine Name','Price','Company Name']
data=[]
# Creates pandas DataFrame.
dataset = pd.DataFrame(data,columns=columns)
dataset


# #### Scraping , then converting scrapped data to dataframe and storing

# In[5]:


# Creating the new row 
for link in all_links:
    for link_item in link:
        if(link_item!='cause'):
            try:
                scraped_data=scrap(link[link_item])
                scraped_flag=1
            except:
                print('Something wrong in scraping')
            data = [        
                    {'Cause':link['cause'],'Medicine Name': scraped_data['medicine_name'],'Price': scraped_data['meidicine_price'],'Company Name': link_item}
                   ]  
            new_row = pd.DataFrame(data)
            dataset = dataset.append(new_row, ignore_index = True)
dataset


# #### Saving dataframe as csv file

# In[6]:


if(scraped_flag==1):
    dataset.to_csv('medicine.csv',index=None )  
    print('Data saved in medicine.csv file')
else:
    print('Scraping failed. So saving data can replace all old data')


# ### Storing data from scraping is closed here

# ### Taking input from User

# In[7]:


input_value=input
("enter the symptoms you face=")


# ### Importing our storage csv file

# In[8]:


storage=pd.read_csv('medicine.csv')
storage


# ### Finding  cause that match to symptoms

# In[9]:


result_data=storage[storage.Cause==input_value]
result_length=len(result_data)
result_data


# #### reseting index of the symptoms

# In[10]:


#reseting index
result_data = result_data.reset_index()
result_data


# ### if result found, preparing data for plotting

# In[11]:


if(result_length==0):
    print('No related data found')
else:
    medicine_name=[]
    medicine_price=[]
    for i in range(result_length):
        title=result_data['Medicine Name'][i]+" ("+result_data['Company Name'][i]+")"
        price=result_data['Price'][i]
        medicine_name.append(title)
        medicine_price.append(price)
print(medicine_name,medicine_price)


# ### Plotting function Call

# In[ ]:


myPlot(medicine_name,medicine_price)


# ### Notification generate For Antibiotics

# In[ ]:


import time
from plyer import notification
import re
for name in medicine_name:
        found=re.search('antibiotic', name)
        if (found):
            notification.notify(
                title = "**Antibiotic Detected!!!",
                message ="Take Medicine Carefully ",
              
                timeout= 10
              )
            time.sleep(60*60)
                
                

