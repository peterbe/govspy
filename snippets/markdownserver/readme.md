Using simple ab (with concurrency):


    $ ab -n 10000 -c 10 http://localhost:XXXX/markdown?body=THis+%2Ais%2A+a+string

Where `XXXX` is the port number depending on which server you're
running.

Results:

    Python (Flask)    2103.06 [#/sec] (mean)
    Python (Tornado)  1834.48 [#/sec] (mean)
    Node (Express)    4406.17 [#/sec] (mean)
    Go                19539.61 [#/sec] (mean)


To run the Go version, first set your `$GOPATH` then:

    $ go get github.com/russross/blackfriday
    $ go run main.go
    $ curl http://localhost:8080/markdown?body=THis+%2Ais%2A+a+string

To run the Tornado versions:

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install tornado mistune markdown
    $ python tornado_.py
    $ curl http://localhost:8888/markdown?body=THis+%2Ais%2A+a+string

To run the Flask version:

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install Flask mistune markdown
    $ python flask_.py
    $ curl http://localhost:5000/markdown?body=THis+%2Ais%2A+a+string

To run the NodeJS version:

    $ npm install  # picks up from package.json
    $ node node_.js
    $ curl http://localhost:3000/markdown?body=THis+%2Ais%2A+a+string
