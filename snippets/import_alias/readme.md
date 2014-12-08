This example is a bit silly because you normally don't bother with an
alias for short built-ins. It's import appropriate for long import
nameslike:

```go
import (
    pb "github.com/golang/groupcache/groupcachepb"
)
```

You can also import packages that you won't actually use. E.g.

```go
import (
    _ "image/png"  // import can do magic
)
```
