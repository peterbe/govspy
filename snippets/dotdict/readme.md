In the Python version you can alternatively be more explicit and use
something like:

```python
initials.setdefault(initial, 0)
```

instead of first checking if the key is there.

Note that in Go, when you set the type to be an `int` it automatically
sets it to 0 upon initialization.
