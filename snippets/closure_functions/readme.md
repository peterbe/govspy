Note in the Python example you can access `number` in the inner function
but you can't change it. Suppose you wanted to do this:

```python

def increment(amount):
    number += amount
increment(1)
increment(2)
```

Then you would get a `UnboundLocalError` error because the variable
would be tied to the inner scope of the `increment` function.
