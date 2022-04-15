# while-loop
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

<div class="thebe-activate"></div>
<div class="thebe-status"></div>

---
## Introduction
While loop is alike if loop, the different is it will loop what inside the loop until the condition become false.

## Example
There is a variable called counter with default value of 0, it will increase 1 after it had been print out. Guess when will it stops.
<pre data-executable="true" data-language="python">
counter = 0
while(counter < 10):
	print(counter)
	counter = counter + 1
</pre>

## A short quiz for you
Replace underlines to make the counter start counting at 5, and stops at 16
<pre data-executable="true" data-language="python">
counter = ___
while(counter < ___):
	print(counter)
	counter __ = counter + 1
</pre>

## Advance quiz
Given to you a random number in variable named randint, please find out the number with while loop and operator. You are forbidded to print to randint out.
<pre data-executable="true" data-language="python">
import random
randint = random.randint(0, 100)
</pre>
