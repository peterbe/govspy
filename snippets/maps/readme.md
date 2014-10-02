You can make a map of maps with:

```
elements : make(map[string]map[string]int)
elements["H"] = map[string]int{
    "protons": 1,
    "neutrons": 0,
}
```

But note, this is what you have `struct` for.
