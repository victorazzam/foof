# Flags of our Fathers

```
    Flags of our Fathers
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

### Version history

* 1.2 - Dec 17 2016 - added file size and permissions
* 1.1 - Dec 15 2016 - added search by contents, added help page
* 1.0 - Dec 01 2016 - added search by name

### License

MIT
