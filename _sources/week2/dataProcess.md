---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Data process and visualize using jupyter book

## Introduction

+++
  Today i will follow insturction from [Interactive Data Analysis with FigureWidget ipywidgets in Python](https://plotly.com/python/figurewidget-app/) to develop a form with HKGov's database.

---
## Importing libararies
```{code-cell} ipython3
import datetime
import numpy as np
import pandas as pd
import requests

import plotly.graph_objects as go
from ipywidgets import widgets
```
---
## Downloading material to process
We will download school list data from HKGov: [School Location and Information](https://data.gov.hk/en-data/dataset/hk-edb-schinfo-school-location-and-information) which contains he names, addresses, coordinates and other relevant information of government, private, aided, Direct Subsidy Scheme, English Schools Foundation and international schools, kindergartens and kindergartens cum-child care centre (as at 28 December 2021). For precise, the file link is: [http://www.edb.gov.hk/attachment/en/student-parents/sch-info/sch-search/sch-location-info/SCH_LOC_EDB.xlsx](http://www.edb.gov.hk/attachment/en/student-parents/sch-info/sch-search/sch-location-info/SCH_LOC_EDB.xlsx)
+++
We will use this file as our raw data and visualize it.
```{code-cell} ipython3
url = 'http://www.edb.gov.hk/attachment/en/student-parents/sch-info/sch-search/sch-location-info/SCH_LOC_EDB.xlsx'
r = requests.get(url, allow_redirects=True)
open('schools.xlsx', 'wb').write(r.content)

df = pd.read_excel('schools.xlsx')
df = df.drop(df.columns[[0]], axis=1)

df.sample(2)
```
---
## Find how many types of school is in HK
To do it, we can use unique() to find out unique item in array.
### Category
```{code-cell} ipython3
schoolTypes = []
chiSchoolTypes = df['ENGLISH CATEGORY'].unique()
for i in range(len(chiSchoolTypes)):
	schoolTypes.append(chiSchoolTypes[i])

tempTable = pd.DataFrame(schoolTypes)
tempTable.columns=['類別']
display(tempTable)
```
+++
### Student Gender
```{code-cell} ipython3
genders = []
chiGenders = df['STUDENTS GENDER'].unique()
for i in range(len(chiGenders)):
	genders.append(chiGenders[i])
	
tempTable = pd.DataFrame(genders)
tempTable.columns=['就讀學生性別']
display(tempTable)
```
+++
### Religion
```{code-cell} ipython3
religions = []
chiReligion = df['RELIGION'].unique()
for i in range(len(chiReligion)):
	religions.append(chiReligion[i])
	
tempTable = pd.DataFrame(religions)
tempTable.columns=['宗教']
display(tempTable)
```
---

## Print out value for each data in tab
```{code-cell} ipython3
def setup_ui(df):
    
    out = widgets.Output()
    with out:
        display(df)
        display(df.plot.barh(x='tag'))
    return out

data = []
row_count = len(df.index)
for i in range(row_count):
  data.append([])
  for item in df.loc[i]:
    data[i].append(item)
ax = []
ay = []
for schoolType in schoolTypes:
  ax.append(schoolType)
  ay.append(0)
  for row in data:
    if(row[0] == schoolType):
      ay[len(ay)-1] += 1
schoolTypeDF = pd.DataFrame({'tag':ax, 'count':ay})

ax = []
ay = []
for gender in genders:
  ax.append(gender)
  ay.append(0)
  for row in data:
    if(row[14] == gender):
      ay[len(ay)-1] += 1
genderDF = pd.DataFrame({'tag':ax, 'count':ay})

tab_contents = ['School Type', 'Student gender']
children = [setup_ui(schoolTypeDF), setup_ui(genderDF)]
tab = widgets.Tab()
tab.children = children
tab.titles = tab_contents
tab
```













