#!/usr/bin/env python
# coding: utf-8

# # Chart.js with Jupyter book - 2
# 
# ## Testing on javascript and ipywidget
# 
# ### Attempt 2

# In[1]:


import ipywidgets as ui
from IPython.core.display import display, HTML

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

# Use ipywidgets HTML for the widget
text = ui.HTML("<p id='tester-p'>Hello World!</p>")   
display(text)


# Still, IPython core is rendered before ipywidgets even we changed the order in script.
# 
# ### Attempt 3

# In[2]:


from IPython.core.display import display, HTML

text = HTML("<p id='tester-p'>Hello World!</p>")   
display(text)

my_script = HTML("""
    <script>
        count = 0;
        widget = document.getElementById("tester-p");
        console.log(widget);
        widget.innerHTML = count;
    </script>

""")

display(my_script)


# Pure IPython core is used, and the result is shown flawlessly.
# 
# ### Attempt 4

# In[3]:


from IPython.core.display import display, HTML

text = HTML("<p id='tester-p'>Hello World!</p>")
button = HTML("<button id='btn' onClick='changeDigit()'>Change</button>")
display(text)
display(button)

my_script = HTML("""
    <script>
        var count = 0;
        function changeDigit(){
          widget = document.getElementById("tester-p");
          console.log(widget);
          count++;
          widget.innerHTML = count;
        }
    </script>

""")

display(my_script)


# The function is working and verified from console, but the innerHTML didn't change.
# 
# ### Attempt 5

# In[4]:


from IPython.core.display import display, HTML

text = HTML("<p id='atm4p'>Hello World!</p>")
button = HTML("<button id='btn' onClick='changeDigit()'>Change</button>")
display(text)
display(button)

my_script = HTML("""
    <script>
        var count = 0;
        function changeDigit(){
          widget = document.getElementById("atm4p");
          console.log(widget);
          count++;
          widget.innerHTML = count;
        }
    </script>

""")

display(my_script)


# Attemp 4 failed because it has shared the same pid with attemp 3. The issue was fixed by change the pid.
