#!/usr/bin/env python
# coding: utf-8

# # Chart.js with Jupyter book
# 
# ## Testing on javascript and ipywidget
# 
# ### Attempt 2

# In[1]:


import ipywidgets as ui
from IPython.core.display import display, HTML

# Use ipywidgets HTML for the widget
text = ui.HTML("<p id='tester-p'>Hello World!</p>")   
display(text)

# Use IPython's HTML for the script
my_script = HTML("""
    <script>
        count = 0;
        widget = document.getElementById("tester-p");
        console.log(widget);
        widget.innerHTML = count;
    </script>

""")

display(my_script)

