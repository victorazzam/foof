#!/usr/bin/python
#
# Locate any file and display its metadata and contents.
# Apparently useful in CTFs ;)
# Might need root in case of restrictions.
#
# Flags of our Fathers ya bish
# Author: Victor Azzam
# License: MIT

import os
from sys import argv, platform

Z = "\033[0m"
R = "\033[91m"
G = "\033[32m"
Y = "\033[93m"
C = "\033[96m"
colors = (C,R,G,Y,R,Y,R,Y,R,Y,G,Y,R,Y,R,C,R,C,Z)

help = """
    %sFlags of our Fathers
 %s.________%so      o%s________.
  %s\/\/\./\/\    %s/_-_-_-_-/
   %s\________\  %s/________/
             %s\%s/
     %sv1.2%s    /%s\\
            %s/  %s\\

    %sAuthor: Victor Azzam
    %s--------------------
        %sLicense: MIT%s

Locate any file and display its metadata and contents.
Usage: %s <option> <string1> [<string2> <string3> ...]

Options:    -n    search file names
            -c    search file contents
            -a    combine options -n and -c

Example 1: %s -n foo bar xyz
Find files containing 'foo' or 'bar' or 'xyz' in their name.

Example 2: %s -a flag
Find files containing 'flag' in their name or contents.
""" % (colors + tuple([argv[0] for i in range(3)]))

found = []
width = int(os.popen("stty size").read().split()[1])

def args():
    tmp = argv[1].lower()
    if tmp in ["-n", "-c", "-a"]:
        return tmp
    print help
    exit(1)

def MDfind(arg, o=""):
    for i in arg:
        a = os.popen("mdfind%s %s" % (o, i)).read().strip().split()
        for x in a:
            if os.path.isfile(x):
                found.append(x)

def meta(F):
    size = os.path.getsize(F)
    P = os.popen("ls -l " + F).read()[1:10]
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
        size, permissions = meta(F)
        print """\n%sContents of %s%s\n%s\n%sSize:     %s bytes\nAccess:   %s%s
%s""" % (R, F, Z, "=" * width, R, size, permissions, Z, "=" * width)
        print Y + "\n".join([x.strip() for x in b if len(x.strip()) > 0]) + Z
        print
        f.close()

def main():
    choice = args()
    arg = argv[2:]
    if choice in ["-n", "-a"]:
        MDfind(arg, " -name")
    if choice in ["-c", "-a"]:
        MDfind(arg)
    if not len(found):
        print "No files found."
        exit()
    final = list(set(found))
    for i in final:
        try:
            stdout(i)
        except IOError:
            print "\nCould not read from '%s'\n" % i
    print """
Total files found: %d
%s
%s
""" % (len(final), "-" * width, "\n".join(final))

if __name__ == "__main__":
    try:
        if len(argv) > 2:
            exit(main())
        print help
    except KeyboardInterrupt:
        print
    exit(1)
