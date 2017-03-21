# multidbq
Simple way of running a single query in multiple Sqlite dbs.

Not optimized for heavy duty use. It's just a helper tool to find information quickly over several DBs.

-----------------------------------------

usage: multidbq.py [-h] [-d ROOT_DIR] [-c CONFIG] [-pf PRINT_FOUND_DBS]
                   [-l LIMIT]
                   query

Multi-DB Sqlite Query Tool

positional arguments:
  query                 Query to execute in multiple DBs

optional arguments:
  -h, --help            show this help message and exit

  -d ROOT_DIR, --root-dir ROOT_DIR
                        Root directory to find DB files in

  -c CONFIG, --config CONFIG
                        Specifies which config file to use

  -pf PRINT_FOUND_DBS, --print-found-dbs PRINT_FOUND_DBS
                        If True, prints all DB files found

  -l LIMIT, --limit LIMIT
                        Limits the number of DBs queried up to the first X
                        specified by this limit


