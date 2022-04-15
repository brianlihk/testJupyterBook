#!/usr/bin/env python
# coding: utf-8

# # Testing on Thebe in jupyterbook
# 
# ## Thebe initaliaztion and configureation
# <script type="text/x-thebe-config"> 
#   {
#       requestKernel: true,
#       mountActivateWidget: true,
#       mountStatusWidget: true,
#       binderOptions: {
#       repo: "binder-examples/requirements",
#       },
#   }
# </script>
# 
# <script src="https://unpkg.com/thebe@latest/lib/index.js"></script>
# ```
# <script type="text/x-thebe-config">
#   {
#       requestKernel: true,
#       mountActivateWidget: true,
#       mountStatusWidget: true,
#       binderOptions: {
#       repo: "binder-examples/requirements",
#       },
#   }
# </script>
# 
# <script src="https://unpkg.com/thebe@latest/lib/index.js"></script>
# ```
# 
# ## Creating activate and run buttons
# <div class="thebe-activate"></div>
# <div class="thebe-status"></div>
# 
# ```
# <div class="thebe-activate"></div>
# <div class="thebe-status"></div>
# ```
# 
# ## Creating executable cell
# <pre data-executable="true" data-language="python">print("Hello!")</pre>
# ```
# <pre data-executable="true" data-language="python">print("Hello!")</pre>
# ```
# 
# ## Details
# We used jupyter lite to perform demostration in python as we don't have a way to attach a cheap and fast kernel into jupyterbook previously. We now have a new solution to be tested if it is worth to use. Binder is a remote kernel to run python scripts on, we can attach one into the page and execute the code in jupyterbook in realtime.
# 
# The script above uses a example binder in the original github repository, and doesn't work everytime while activating the binder. I will try to fork one into my repo, hoping to reduce any confliction or unknown error with other user during runtime. I will change the repo into my forked one on the next page.
