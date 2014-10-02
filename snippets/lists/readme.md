A `slice` is a segment of an array whose length can change.

The major difference between an `array` and a `slice` is that with the
array you need to know the size up front. In Go, there is no way to
equally easily add values to an existing `slice` so if you want to
easily add values, you can initialize a slice at a max length and
incrementally add things to it.
