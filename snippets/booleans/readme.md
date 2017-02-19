Go doesn't have a quick way to evaluate if something is
["truthy"](http://en.wikipedia.org/wiki/Truthiness).
In Python, for example, you can use an `if` statement on any type and
most types have a way of automatically converting to `True` or
`False`. For example you can do:

```python
x = 1
if x:
    print "Yes"
y = []
if y:
    print "this won't be printed"
```

This is not possible in Go. You really need to do it explicitly for
every type:

```go
x := 1
if x != 0 {
	fmt.Println("Yes")
}
var y []string
if len(y) != 0 {
	fmt.Println("this won't be printed")
}
```
