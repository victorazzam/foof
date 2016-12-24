#!/usr/bin/python
#
# Locate any file and display its metadata and contents.
# Might need root in case of restrictions.
# Apparently useful in CTFs ;)
#
# Flags of our Fathers ya bish
# Author: Victor Azzam
# License: MIT

import os
import time
from sys import argv, platform

Z = "\033[0m"
R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
C = "\033[96m"
colors = (C,R,G,Y,R,Y,R,Y,R,Y,G,Y,R,Y,R,C,R,C,Z)

logo = """
    %sFlags of our Fathers
 %s.________%so      o%s________.
  %s\/\/\./\/\    %s/_-_-_-_-/
   %s\________\  %s/________/
             %s\%s/
     %sv1.5%s    /%s\\
            %s/  %s\\

    %sAuthor: Victor Azzam
    %s--------------------
        %sLicense: MIT%s

Locate any file and display its metadata and contents.
""" % colors

help = logo + """
USAGE
-----
%s <option> <string> [<string> ...]

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
""" % argv[0]

examples = logo + """
EXAMPLES
--------
%s -n foo bar xyz
Find files containing 'foo' or 'bar' or 'xyz' in their name.

%s -c flag
Find files containing 'flag' in their name or contents.

%s -d list
Find directories containing 'list' in their name.

%s -a daemon
Find directories containing 'daemon' in their name, and files
containing 'daemon' in their name or contents.
""" % tuple([argv[0] for x in range(4)])

found = []
width = int(os.popen("stty size").read().split()[1])

def args():
    tmp = argv[1]
    if tmp in ["-e", "-n", "-c", "-d", "-a", "-nl", "-cl", "-dl", "-al"]:
        if argv[1] == "-e":
            exit(examples)
        else:
            if platform != 'darwin' and tmp in ['-c', '-cl']:
                exit("Unfortunately your system does not support searching by content, sorry about that :(")
            return tmp
    else:
        exit(help)

# Limited indexing system that replaces mdfind for those who don't have it.
def index(paths_):
    files = []
    dirs = paths_
    for path in dirs:
        try:
            for i in os.listdir(path):
                i = path.rstrip('/') + '/' + i.strip('/')
                if os.path.isfile(i):
                    files.append(i)
                elif os.path.isdir(i):
                    dirs.append(i)
        except (IOError, OSError):
            pass
    return sorted(files), sorted(dirs)

def index_sort(index_src, o):
    if index_src[0].startswith(('/home/', '/root/')):
        del index_src[0]
    index_n, index_d = index(index_src)
    if o == 'f':
        return index_n
    if o == 'd':
        return index_d
    return index_n + index_d

def MDfind(choice, arg, o=""):
    if platform != 'darwin':
        paths = [os.path.expanduser('~'), '/home', '/root', '/usr/bin', '/usr/local/bin', '/etc']
        indexed = index_sort(paths, o)
    for i in arg:
        if platform != 'darwin':
            for x in indexed:
                if i.lower() in x.rstrip('/').split('/')[-1].lower():
                    found.append(x)
        else:
            a = os.popen("mdfind%s %s" % (o, i)).read().strip().split("\n")
            for x in a:
                if choice in ["-d", "-dl"]:
                    if not os.path.isdir(x):
                        continue
                if choice in ["-n", "-c", "-nl", "-cl"]:
                    if not os.path.isfile(x):
                        continue
                found.append(x)

def meta(F):
    size = os.path.getsize(F)
    P = oct(os.stat(F).st_mode & 0777)[-3:]
    perm = int(P[2])
    if os.geteuid() == os.stat(F).st_uid:
        perm = int(P[0])
    rwx = ["read", "write", "execute"]
    if perm != 7:
        if perm == 6:
            del rwx[2]
        if perm == 5:
            del rwx[1]
        if perm == 4:
            del rwx[1:]
        if perm == 3:
            del rwx[0]
        if perm == 2:
            rwx = [rwx[1]]
        if perm == 1:
            del rwx[0:2]
        if not perm:
            rwx = []
    perm = "none"
    if len(rwx):
        perm = ", ".join(rwx)
    return size, perm

def stdout(F):
    error = 0
    try:
        f = open(F)
        b = f.read().strip().split("\n")
        b = [x.strip() for x in b if len(x.strip()) > 0]
        f.close()
    except (IOError, OSError):
        error = 1
        b = "Could not read from '%s'" % F
        if os.path.isdir(F):
            b = "'%s' is a directory." % F
    size, permissions = meta(F)
    print """\n%sContents of %s%s\n%s\n%sSize:     %s bytes\nAccess:   %s%s
%s""" % (G, F, Z, "=" * width, R, size, permissions, Z, "=" * width)
    if not error:
        if size > 250:
            print "File too large, printing first 250 characters.\n" + "-" * 46
            print Y + "\n".join(b)[:250] + Z
        else:
            print Y + "\n".join(b) + Z
    else:
        print b
    time.sleep(0.1) # Partially prevents excessive CPU usage.

def main():
    choice = args()
    arg = argv[2:]
    if platform == 'darwin':
        if choice in ["-n", "-d", "-nl", "-dl"]:
            o = ' -name'
        elif choice in ["-c", "-a", "-cl", "-al"]:
            o = ''
    else:
        if choice in ["-n", "-nl"]:
            o = 'f'
        elif choice in ['-d', '-dl']:
            o = 'd'
        else:
            o = ''
    MDfind(choice, arg, o)
    if not len(found):
        exit("No files found.")
    final = list(set(found))
    if not choice.endswith("l"):
        for i in final:
            stdout(i)
    print """
Total files found: %d
%s
%s%s%s
""" % (len(final), "-" * width, G, "\n".join(final), Z)

if __name__ == "__main__":
    try:
        if len(argv) > 1:
            exit(main())
        print help
    except KeyboardInterrupt:
        print
