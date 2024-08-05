#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import requests
#API to fetch temperature of city 
city_name=input("Enter city name:")
api_key='9eb851d3864ea2437df66351176c2783'
#To build URL api
api_url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
get_server_information=requests.get(api_url)
print(get_server_information.json())


# In[ ]:




