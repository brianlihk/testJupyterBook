#!/usr/bin/env python
# coding: utf-8

# # How to create a executable page in jupyter book (17 Jan 2022)
# 
# ## Introduction
# 
# In order to make a page executable, we will need some work to do it.
# 
# ---
# 
# ## Prepare the .md file
# 
# To make the code executable, we will need to add front-matter YAML block to state to the machine that we are using python3 code.
# 
# Add this block on top of your .md file so the file recognize it as a executable page.
# ```
# ---
# jupytext:
#   formats: md:myst
#   text_representation:
#     extension: .md
#     format_name: myst
# kernelspec:
#   display_name: Python 3
#   language: python
#   name: python3
# ---
# ```
# 
# When we need to make a executable code, we need to code inside the code-cell, the format of the code-cell is like below:
# 
# ````md
# ```{code-cell} ipython3
# 
# ```
# ````
# 
# We can put python code into the space in the middle and it will execute and return result for us below the cell
# 
# 
# ## Have some fun with it!
# 
# ```{note}
# Lets make some fun on this block and try to print out some message!
# ```
# ````md
# ---
# jupytext:
#   formats: md:myst
#   text_representation:
#     extension: .md
#     format_name: myst
# kernelspec:
#   display_name: Python 3
#   language: python
#   name: python3
# ---
# 
# ```{code-cell} ipython3
# from datetime import datetime
# 
# now = datetime.now()
# 
# print(f'This is a message executed at {now.strftime("%d/%m/%Y %H:%M:%S")}')
# ```
# ````
# 
# Result:

# In[1]:


from datetime import datetime

now = datetime.now()

print(f'This is a message executed at {now.strftime("%d/%m/%Y %H:%M:%S")}')

