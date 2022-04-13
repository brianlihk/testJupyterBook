# Download required library into our kernel

## The start
Since I am using binder in my own repository, i drilled into the files in the forked repository and found a file called requirements.in with package names that is installed by default. I can just add any package i want into the file and it should be downloaded when the kernel is being activated.

```{figure} ./commiting.png
:name: Commiting the changes in github
```
## After commiting change on requirements.in of my repository
But this doesn't work well. It doesn't install the package into the kernel. Instead, I found a way to do the job more easily. We can just use !pip install [package name] and wala it's gonna install automatically.

## Thebe initaliaztion and configureation
<script type="text/x-thebe-config"> 
  {
      requestKernel: true,
      mountActivateWidget: true,
      mountStatusWidget: true,
      binderOptions: {
      repo: "brianlihk/requirements",
      },
  }
</script>

<script src="https://unpkg.com/thebe@latest/lib/index.js"></script>
```
<script type="text/x-thebe-config">
  {
      requestKernel: true,
      mountActivateWidget: true,
      mountStatusWidget: true,
      binderOptions: {
      repo: "brianlihk/requirements",
      },
  }
</script>

<script src="https://unpkg.com/thebe@latest/lib/index.js"></script>
```

## Creating activate and run buttons
<div class="thebe-activate"></div>
<div class="thebe-status"></div>

```
<div class="thebe-activate"></div>
<div class="thebe-status"></div>
```
## Exmaples
### Import test
<pre data-executable="true" data-language="python">
!pip install art
from art import *
Art=text2art("art")
print(text2art('''Ayo
Wasup
''', font="small"))
</pre>

Success

