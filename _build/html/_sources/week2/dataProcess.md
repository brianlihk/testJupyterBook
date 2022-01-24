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

# Data process and visualize using jupyter book - 1(24 Jan 2021)

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
chiSchoolTypes = df['中文類別'].unique()
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
chiGenders = df['就讀學生性別'].unique()
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
chiReligion = df['宗教'].unique()
for i in range(len(chiReligion)):
	religions.append(chiReligion[i])
	
tempTable = pd.DataFrame(religions)
tempTable.columns=['宗教']
display(tempTable)
```
---

### We also need to get numbers on each data
```{code-cell} ipython3
data = []
for row in df.loc():
  data_row = []
  for col_data in row:
    data_row.append(col_data)
print(data)
```













