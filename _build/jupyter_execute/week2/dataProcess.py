#!/usr/bin/env python
# coding: utf-8

# # Data process and visualize using jupyter book
# 
# ## Introduction
# Today i will follow insturction from [Interactive Data Analysis with FigureWidget ipywidgets in Python](https://plotly.com/python/figurewidget-app/) to develop a form with HKGov's database.
# ---
# ## Importing libararies

# In[1]:


import datetime
import numpy as np
import pandas as pd
import requests

import plotly.graph_objects as go
from ipywidgets import widgets


# ---
# ## Downloading material to process
# We will download school list data from HKGov: [School Location and Information](https://data.gov.hk/en-data/dataset/hk-edb-schinfo-school-location-and-information) which contains he names, addresses, coordinates and other relevant information of government, private, aided, Direct Subsidy Scheme, English Schools Foundation and international schools, kindergartens and kindergartens cum-child care centre (as at 28 December 2021). For precise, the file link is: [http://www.edb.gov.hk/attachment/en/student-parents/sch-info/sch-search/sch-location-info/SCH_LOC_EDB.xlsx](http://www.edb.gov.hk/attachment/en/student-parents/sch-info/sch-search/sch-location-info/SCH_LOC_EDB.xlsx)

# We will use this file as our raw data and visualize it.

# In[2]:


url = 'http://www.edb.gov.hk/attachment/en/student-parents/sch-info/sch-search/sch-location-info/SCH_LOC_EDB.xlsx'
r = requests.get(url, allow_redirects=True)
open('schools.xlsx', 'wb').write(r.content)

df = pd.read_excel('schools.xlsx')
df = df.drop(df.columns[[0]], axis=1)

df.sample(3)

