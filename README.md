# Flags of our Fathers

***

### Description

A python script that uses the help of `mdfind` and prints whatever files

### Usage

Grant execution permissions first:
`$ chmod 777 foof`

Then run foof like this:
`$ ./foof`

The help screen:
```
Usage: ./foof <option> <string1> [<string2> <string3> ...]

Options:    -n    search file names
            -c    search file contents
            -a    combine options -n and -c

Example 1: ./foof -n foo bar xyz
Find files containing 'foo' or 'bar' or 'xyz' in their name.

Example 2: ./foof -a flag
Find files containing 'flag' in their name or contents.
```
