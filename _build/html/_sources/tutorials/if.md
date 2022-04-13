# if-loop
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

## if
Computer are dump, they dont know what to do if you don't write it into their language.
For example, we want python to print something if the user is older than 18, we can use if-loop in python, see the example and enter 19 as your age:

<pre data-executable="true" data-language="python">
age = int(input("Tell me your age please"))
if(age > 18):
	print("OK, you can come into here.")
</pre>

After you give your age to python, it will print something when you have enter a value greater than 18.

## if else

But notice that it will do nothing when you are not older than 18, so here is when this else function comes in. We can tell python to do something else when the condition isn't match. Enter 15 as your age

<pre data-executable="true" data-language="python">
age = int(input("Tell me your age please"))
if(age > 18):
	print("OK, you can come into here.")
else:
	print("Please keep out of this area.")
</pre>

It can ban you from going into prohibited area now!

## if elif else
What if you want it to maybe let some 17 years old come in exclusively? you can use elif!
Enter 17 as your age
<pre data-executable="true" data-language="python">
age = int(input("Tell me your age please"))
if(age > 18):
	print("OK, you can come into here.")
elif(age == 17):
	print("Fine, this time only.")
else:
	print("Please keep out of this area.")
</pre>

That works flawlessly!

## A short quiz for you
### Fill in blanks
By now you should know how to use if, try to replace underlines to complete the script!
<pre data-executable="true" data-language="python">
age = int(input("Tell me your age please"))
____:(age > 18):
	print("_____")
____(age == 17):
	print("_____")
____:
	print("_____")
</pre>
## Creative idea time
Below is a playground for you to use, feel free to mess around
<pre data-executable="true" data-language="python">
age = int(input("Tell me your age please"))

</pre>
