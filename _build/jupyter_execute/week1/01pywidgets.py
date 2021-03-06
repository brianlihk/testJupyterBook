#!/usr/bin/env python
# coding: utf-8

# # Learning on ipywidgets (19 Jan 2022)
# 
# ## Slider
# ### import packages
# We will import ipywidgets as widgets

# In[1]:


import ipywidgets as widgets


# ---
# ### initalize the slider
# We can initialize a Intslider with widgets

# In[2]:


slider = widgets.IntSlider()


# ---
# ### Display the widget
# We can display the slider with Display package

# In[3]:


from IPython.display import display
display(slider)


# ---
# ### Close the widget
# We can close it with widget.close()

# In[4]:


#slider.close()


# - But once we closed it, some bug apperas and it won't show up the widget but text instead
# ---
# ### Changing the value
# We can get/set the value of the widget

# In[5]:


slider.value = 50
display(slider)


# ---
# ### jslink
# we can link the value of different widget by jslink

# In[6]:


a = widgets.FloatText()
b = widgets.FloatSlider()
display(a,b)

mylink = widgets.jslink((a, 'value'), (b, 'value'))


# ---
# ## Types of Widgets
# ### Numeric widgets
# There are so many types of numeric widgets we can use, including:
# - IntSlider
# - FloatSlider
# - FloatLogSlider
# - IntRangeSlider
# - FloatRangeSlider
# - IntProgress
# - FloatProgress
# - BoundedIntText
# - BoundedFloatText
# - IntText
# - FloatText
# 	Referece: [Jupyter Widgets/Widget List/Numeric widgets](https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html#Numeric-widgets)
# ---
# ### Boolean widgets
# - ToggleButton
# - Checkbox
# - Valid
# 	Referece: [Jupyter Widgets/Widget List/Boolean widgets](https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html#Boolean-widgets)
# ---
# ### Selection widgets
# - Dropdown
# - RadioButtons
# - Select
# - SelectionSlider
# - SelectionRangeSlider
# - ToggleButtons
# - SelectMultiple
# 	Referece: [Jupyter Widgets/Widget List/Selection widgets](https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html#Selection-widgets)
# ---
# ### String widgets
# - Text
# - Textarea
# - Password
# 	Referece: [Jupyter Widgets/Widget List/String widgets](https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html#String-widgets)
# ---
# ## How to combine widgets into one
# If we want to combine a widget, we will need to use a widget called HBox.
# For example, if we want to combine a label and a slider bar together, we can do:

# In[7]:


widgets.HBox([widgets.Label(value="The $m$ in $E=mc^2$:"), widgets.FloatSlider()])


# * And i assume the H in HBox stands for horizontal.
# ---
# ## Print out image with python
# We can use Image widget to print out the file in specified path. For example:

# In[8]:


file = open("../rick.jpg", "rb")
image = file.read()
widgets.Image(
    value=image,
    format='jpg',
)


# * And please note that the root directory is the base of the file, so if you want to access file under you book's root folder, you will need to use relative path to access it.
# 
# ---
# ```{warning}
# Sample beyond this warning is unstable, i am still looking for a way to do front end execute
# ```
# ---
# ## Output

# In[9]:


import ipywidgets as widgets
val = 2
inp = widgets.IntSlider(value = val, min = 1, max = 10, 
                        description = 'x', readout = False)
out = widgets.Label(r'\({0}^2 = {1}\)'.format(val,val*val))
def handle_inp_change(value):
    out.value = r'\({0}^2 = {1}\)'.format(value.new,value.new*value.new)
inp.observe(handle_inp_change,'value')
display(widgets.HBox([inp,out]))


# ---
# ## Creating and binding a button to a python function
# We can create button in ipywidgets, and make it call a function whenever it is clicked. For example:

# In[10]:


def printOutText(txt):
	print(txt)
output = widgets.Output()
button = widgets.Button(
    description='Click me',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Click me',
    icon='check' # (FontAwesome names without the `fa-` prefix)
)
text_field = widgets.Text(
    value='Hello World',
    placeholder='Text',
    description='Message you want to print:',
    disabled=False
)
button.on_click(printOutText, text_field.value)
row = widgets.HBox([text_field, button])
display(row, output)


# In[11]:


from IPython.display import display
import sys
button = widgets.Button(description="Click Me!")
output = widgets.Output()

display(button, output)

def on_button_clicked(b):
    print('clicked', file=sys.stderr)
    with output:
        print("Button clicked.", file=sys.stderr)

button.on_click(on_button_clicked)


# ```{note}
# changed the format form .md to ipynb, and it still donesn't work at the end of the day.
# will look for other method of fix next day.
# ```
