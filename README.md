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

Compatibility: macOS, BSD (honestly no clue)

Note: A version compatible with GNU/Linux will be worked on and released in this repo and named foof-gnu.py (for unknown reasons). Sad to see Linux without a centrally managed database of files (such as Spotlight on macOS), gonna have to find a way to replicate `mdfind`'s functionality. UGH!

### ¡Something Important!
```diff
- So apparently... I just realised this doesn't work on _actual_ GNU/Linux, rather only
- on BSD-derived and Darwin systems. Sorry to all who have been mind boggled by the
- 'mdfind: not found' message (if you've got to that stage). Either way it still has its
- place as the OSes it supports will (slowly, but steadily) become a greater part of the
- hacking scene. Further apologies for the confusion.
```

### Usage

Grant execution permissions first:

`$ chmod 777 foof.py`

Then run foof like this:

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

### Latest update

I somehow managed to create an indexing method for GNU/Linux systems without the need for another release. In the interest of time and computing resources, it currently only indexes:

* $USER's home dir, if it's not [/root] or [in /home]
* /root
* /home
* /usr/bin
* /usr/local/bin

No significant timeouts so I think it's a good start. The algorithm has been verified and it works on Debian and its derivatives. Now it's all down to how much CPU potency and time you've got on your hands.

Release date for version 1.5 is Dec 21 2016 so don't run away just yet! Hehe

### Version history

* 1.4 - Dec 19 2016 - more search options, more output options, bug fixes
* 1.3 - Dec 18 2016 - truncate output of large files, fixed filename issue
* 1.2 - Dec 17 2016 - file size and permissions
* 1.1 - Dec 15 2016 - search by contents, help page
* 1.0 - Dec 01 2016 - search by name

### License

MIT
