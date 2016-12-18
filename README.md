# Flags of our Fathers

```
                 .________o      o________.
                  \/\/\./\/\    /_-_-_-_-/
                   \________\  /________/
                             \/
                             /\
                            /  \
```

### Description

A python script that uses the help of `mdfind` to search and display any file's metadata and contents based on a given string.

Compatibility: Linux and macOS

### Usage

Grant execution permissions first:

`$ chmod 777 foof.py`

Then run foof like this:

`$ ./foof.py`

### Help

```
Usage: ./foof.py <option> <string1> [<string2> <string3> ...]

Options:    -n    search file names
            -c    search file contents
            -a    combine options -n and -c

Example 1: ./foof.py -n foo bar xyz
Find files containing 'foo' or 'bar' or 'xyz' in their name.

Example 2: ./foof.py -a flag
Find files containing 'flag' in their name or contents.
```

### Latest update

Dealt with output to give the OS some time to print the contents. Also, changed output trimming from 50 lines to 250 characters.

### Version history

* 1.4 - Dec 19 2016 - more search options, more output options, bug fixes
* 1.3 - Dec 18 2016 - truncate output of large files, fixed filename issue
* 1.2 - Dec 17 2016 - file size and permissions
* 1.1 - Dec 15 2016 - search by contents, help page
* 1.0 - Dec 01 2016 - search by name

### License

MIT
