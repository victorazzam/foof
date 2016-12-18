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
     %sv1.4%s    /%s\\
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
            print examples
        else:
            return tmp
    else:
        print help
    exit(1)

def MDfind(choice, arg, o=""):
    for i in arg:
        a = os.popen("mdfind%s %s" % (o, i)).read().strip().split("\n")
        for x in a:
            if choice in ["-d", "-dl"]:
                if not os.path.isdir(x):
                    continue
            elif choice in ["-n", "-c", "-nl", "-cl"]:
                if not os.path.isfile(x):
                    continue
            elif choice in ["-a", "-al"]:
                pass
            found.append(x)

def meta(F):
    size = os.path.getsize(F)
    P = os.popen("ls -l " + F.replace(" ", "\ ")).read()[1:10]
    perm = P[-3:]
    if os.geteuid() == os.stat(F).st_uid:
        perm = P[:3]
    rwx = []
    if "r" in perm:
        rwx.append("read")
    if "w" in perm:
        rwx.append("write")
    if "x" in perm:
        rwx.append("execute")
    perm = "none"
    if len(rwx) > 0:
        perm = ", ".join(rwx)
    return size, perm

def stdout(F):
    with open(F) as f:
        b = f.read().strip().split("\n")
        b = [x.strip() for x in b if len(x.strip()) > 0]
        size, permissions = meta(F)
        print """\n%sContents of %s%s\n%s\n%sSize:     %s bytes\nAccess:   %s%s
%s""" % (G, F, Z, "=" * width, R, size, permissions, Z, "=" * width)
        if size > 250:
            print "File too large, printing first 250 characters.\n" + "-" * 46
            print Y + "\n".join(b)[:250] + Z
        else:
            print Y + "\n".join(b) + Z
        time.sleep(0.1)
        f.close()

def main():
    choice = args()
    arg = argv[2:]
    if choice in ["-n", "-d", "-nl", "-dl"]:
        MDfind(choice, arg, " -name")
    elif choice in ["-c", "-a", "-cl", "-al"]:
        MDfind(choice, arg)
    if not len(found):
        print "No files found."
        exit()
    final = list(set(found))
    if not choice.endswith("l"):
        for i in final:
            try:
                stdout(i)
            except IOError:
                if not os.path.isdir(i):
                    print "\nCould not read from '%s'\n" % i
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
    exit(1)
