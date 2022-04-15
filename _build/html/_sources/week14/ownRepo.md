# Tesing on Thebe with own repository in github

## Before we start
As i mentioned in the last attemp, i forked a same copy of the repo we are using in last page. I will reconfig the thebe and make some try fly with it.

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

## Creating executable cell
<pre data-executable="true" data-language="python">print("Hello!")</pre>
```
<pre data-executable="true" data-language="python">print("Hello!")</pre>
```

## Other exmaples
### Calcalation test
<pre data-executable="true" data-language="python">
import math
# Assign values to x and n
x = 4
n = 3

# Method 1
power = x ** n
print("%d to the power %d is %d" % (x,n,power))

# Method 2
power = pow(x,n)
print("%d to the power %d is %d" % (x,n,power))

# Method 3
power = math.pow(2,6.5)
print("%d to the power %d is %5.2f" % (x,n,power))
</pre>

Success
### Input test
<pre data-executable="true" data-language="python">
# Define the number set
numbers = {23, 90, 56, 78, 12, 34, 67}
 
# Add a new data
numbers.add(50)
# Print the set values
print(numbers)

message = "Number is not found"

# Take a number value for search
search_number = int(input("Enter a number:"))
# Search the number in the set
for val in numbers:
    if val == search_number:
        message = "Number is found"
        break

print(message)
</pre>

Success
### Import test
<pre data-executable="true" data-language="python">
# Import another python script
import vacation as v

# Initialize the month list
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
# Initial flag variable to print summer vacation one time
flag = 0

# Iterate the list using for loop
for month in months:
    if month == "June" or month == "July":
        if flag == 0:
            print("Now",v.vacation1)
            flag = 1
    elif month == "December":
            print("Now",v.vacation2)
    else:
        print("The current month is",month)
</pre>

Failed, there is no lib installed.

## Details
The script failed when it is importing a non-existing library, I will find a way t ofix it as i can foresee there will be tons of packages to be installed for wide range of usage.