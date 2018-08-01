# Flags of our Fathers

```
                 .________o v2.0 o________.
                  \/\/\./\/\    /_-_-_-_-/
                   \________\  /________/
                             \/
                             /\
                            /  \
```

### Description

Locate any file by name or contents with finely grained controls.

Note 1: regular expressions not supported (yet)

Note 2: not tested on Windows

### Setup

Install dependency `ag` from http://github.com/ggreer/the_silver_searcher

Install `foof`:

```txt
$ git clone https://github.com/victorazzam/foof.git
$ cd foof-master
$ mv foof.py foof
$ chmod a+x foof
```

Finally run foof like this:

`$ ./foof --help`

### Usage

```
usage: foof [options] <string> [string ...]

positional arguments:
  string                the search keyword(s), space separated if >1

optional arguments:
  -h, --help            show this help message and exit
  -b n|c|a, --by n|c|a  search by: n = name (default), c = contents, a = n + c
  -i, --case            ignore case when searching
  -p path, --path path  root search directory, default = $HOME
  -d num, --depth num   search <num> directories deep, default = 0 (recursive)
  -a 0-7, --access 0-7  filter by access rights, e.g. 5 matches r-x
  -v, --version         show version and exit
```

### Latest changes

* The contents search is now done by `ag`
* Specify search path
* Search by permissions
* Customise search depth
* Control case sensitivity
* Can be used as a library: `from foof import find`
* Linear pipeable output

### Version history

* 2.0 - Aug 01 2018 - completely rewritten, see changelog
* 1.5 - Dec 24 2016 - GNU/Linux support, directory permissions issue fixed
* 1.4 - Dec 19 2016 - more search options, more output options, bug fixes
* 1.3 - Dec 18 2016 - truncate output of large files, fixed filename issue
* 1.2 - Dec 17 2016 - file size and permissions
* 1.1 - Dec 15 2016 - search by contents, help page
* 1.0 - Dec 01 2016 - search by name

### License

MIT
