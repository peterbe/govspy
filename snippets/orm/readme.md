This is a comparison between
[gorp](https://github.com/coopernurse/gorp) and
[sqlalchemy](http://www.sqlalchemy.org/).

Using `pq` and `psycopg2` it creates a bunch of ORM instance objects,
then edits them all one by one and then deletes them all. This example
assumes PostgreSQL and that the table already exists.

It creates X number of "talks" which has the following column types:

1. id serial integer
2. topic varchar(200)
3. when timestamp
4. tags array of text
5. duration real

Then lastly it measures how long it takes to do all the inserts, all the
updates and all the deletes.

When running these for **10,000 iterations** on my computer I get the
following outputs:

    $ python orm.py
    insert 3.09894585609
    edit 30.3197979927
    delete 18.6974749565
    TOTAL 52.1162188053

    $ go run orm.go
    insert 2.542336905s
    edit 10.28062312s
    delete 6.851942699s
    TOTAL 19.674902724s
