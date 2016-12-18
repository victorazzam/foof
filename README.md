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

### Latest update

Fixed an issue where some files were ignored due to incorrect string handling.

### Version history

* 1.3 - Dec 18 2016 - only print 50 lines per file, fix for files with spaces
* 1.2 - Dec 17 2016 - file size and permissions
* 1.1 - Dec 15 2016 - search by contents, help page
* 1.0 - Dec 01 2016 - search by name

### License

MIT
