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
# Chart.js with Jupyter book - 1

## Testing on javascript and ipywidget

### Attempt 1
```{code-cell} ipython3
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
```

widget variable not found

After inspected into source code, i found that the p element was defined after script, so it will not work.

HTML is rendered before ui.HTML