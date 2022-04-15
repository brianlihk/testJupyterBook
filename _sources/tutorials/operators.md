# Operators (WIP)
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
Operator could help computer to decide if A and B value is true or false in operator.
For example 1 is greater than 0, we can express it as 1>0, python will return us a true value. But if we try 0>1, the result will be false as it is a false statement.

## Operator form
There are three types of operator, one for calcalating called Aritgmetic operator. Another one called comparison were for comparing left and right side to return if it is a true or false statement.

### Arithmetic
| operator | explain | example | japanese |
| :------: | :------ | :------ | :------: |
| + | add | a + b | 加算 |
| - | subtract | a - b | 減算 |
| * | multiply | a * b | 乗算 |
| / | devide | a / b | 除算 |
| % | modulus. This will return the leftover value when b devided by a | a % b | 余り |
### Comparison
| operator | explain | example |
| :------: | :------ | :------ |
| > | greater than | a > b |
| >= | greater or equal to | a >= b|
| < | less than | a < b |
| <= | less or equal to | a <= b |
| == | equal to | a == b |
| != | not equal to | a != b |
| ! | not | !a == !b |

### Logical
| operator | exlain | example |
| and | return True when both a and b are true, else return False | a and b |
| or | return True when any of a or b is True, unless they are both False | a or b |
| not | return the opposite state | not a |

## Example

### Arithmetic
<pre data-executable="true" data-language="python">
a = 10
b = 6

print(a+b)
print(a-b)
print(a*b)
print(a/d)
print(a%b)
</pre>

### Comparison
<pre data-executable="true" data-language="python">
a = 10
b = 6

print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a == b)
print(a != b)
print(!a)
print(a%b)
</pre>

### Logic
<pre data-executable="true" data-language="python">
a = True
b = False

print(a and b)
print(a or b)
print(a and not b)
print(not a and b)
</pre>

## A short quiz for you
1. replace the underline to any operator that you think are appropriate to make the output as true.

<pre data-executable="true" data-language="python">
a = ____
b = ____
c = ____

print(((a and b) and not c) or a)
</pre>


## Creative idea time
Below is a playground for you to use, feel free to mess around
<pre data-executable="true" data-language="python">

</pre>