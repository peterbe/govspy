The Python version is neat in that it's entirely type agnostic as long as
the value supports hashing.
I'm sure it's possible to do an equivalent one in Go using `interface{}`.
Patches welcome.

For faster variants in Python see
[Fastest way to uniqify a list in
Python](http://www.peterbe.com/plog/uniqifiers-benchmark).

For some more thoughts on this, and an example of a implementation
that is not in-place check out [this mailing list
thread](https://groups.google.com/d/topic/golang-nuts/-pqkICuokio/discussion).
