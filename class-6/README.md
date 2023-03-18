# Ojectives of this lession - Class - 6

# range

## Definition and Usage
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

```
range(start, stop, step)
```

start	Optional. An integer number specifying at which position to start. Default is 0
stop	Required. An integer number specifying at which position to stop (not included).
step	Optional. An integer number specifying the incrementation. Default is 1

```
x = range(3, 20, 2)
for n in x:
  print(n)
```