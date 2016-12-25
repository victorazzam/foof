# Flags of our Fathers

```
                 .________o v1.5 o________.
                  \/\/\./\/\    /_-_-_-_-/
                   \________\  /________/
                             \/
                             /\
                            /  \
```

### Description

A python script that uses the help of `mdfind` and a custom indexing system to search and display any file's metadata and contents based on a given string.

Compatibility: macOS, Linux

```diff
+ Comparison table below.
```

### Setup

Download and grant execution permissions:

```txt
$ git clone https://github.com/victorazzam/foof.git
$ cd foof-master
$ chmod a+x foof.py
```

Finally run foof like this:

`$ ./foof.py`

### Help

```
USAGE
-----
./foof.py <option> <string> [<string> ...]

OPTIONS
-------
-n    search file names
-c    search file names and contents
-d    search directory names
-a    combine options -n, -c and -d
-e    show examples for each option

Note: append 'l' to the end of any option apart from -e
      (-nl, -cl, etc...) to only display the locations
      without the metadata and contents.
```

### Comparison table

|           OS           | macOS                                                                                         | GNU/Linux                                                                     |
|:----------------------:|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
|   Search terms filter  | start/end of the name, or after a special character (e.g. "flag" returns: \*flag & flag\* & \*–flag\*) | any part of the name                                                          |
|     Content search     | Supported                                                                                     | Not supported                                                                 |
|        Indexing        | Entire filesystem: mdfind (pre-made, always up-to-date)                                               | /root, /home, /usr/bin, /usr/local/bin, /etc: custom (live, at the start of each run) |
|          Speed         | Fastest                                                                                       | Medium (depends on the CPU)                                                   |
| Superuser requirements | None                                                                                          | Needs "root" to list protected files/dirs                                     |

### Latest update

- [x] Comparison table added.

### Version history

* 1.5 - Dec 24 2016 - GNU/Linux support, directory permissions issue fixed
* 1.4 - Dec 19 2016 - more search options, more output options, bug fixes
* 1.3 - Dec 18 2016 - truncate output of large files, fixed filename issue
* 1.2 - Dec 17 2016 - file size and permissions
* 1.1 - Dec 15 2016 - search by contents, help page
* 1.0 - Dec 01 2016 - search by name

### License

MIT
