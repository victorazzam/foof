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

A python script that uses the help of `mdfind` to search and display any file's location and contents based on a given string.

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

### License
MIT
