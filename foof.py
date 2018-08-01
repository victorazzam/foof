#!/usr/bin/env python3
#
# Useful shell search command:
# $ find /search/path -maxdepth 1 -not -type d -exec grep -li 'search_term_or_regex' {} \+
#
# Flags of our Fathers v2
# Author: Victor Azzam
# License: MIT

import argparse

v = "2.0"
d = "1 August 2018"
r = "https://victorazzam.github.io/foof"

NAME = "FooF"
USGE = "foof [options] <string> [string ...]"
DESC = f"Locate files by name or contents ({r})"
ELOG = "Content search dependency: ag (http://github.com/ggreer/the_silver_searcher)"
HELP_type = "search by: n = name (default), c = contents, a = n + c"
HELP_case = "ignore case when searching"
HELP_path = "root search directory, default = $HOME"
HELP_dpth = "search <num> directories deep, default = 0 (recursive)"
HELP_axes = "filter by access rights, e.g. 5 matches r-x"
parser = argparse.ArgumentParser(prog=NAME, usage=USGE, description=DESC, epilog=ELOG)
parser.add_argument("string", nargs="+", help="the search keyword(s), space separated if >1")
parser.add_argument("-b", "--by", choices=list("nca"), default="n", help=HELP_type, metavar="n|c|a")
parser.add_argument("-i", "--case", action="store_true", help=HELP_case)
parser.add_argument("-p", "--path", nargs=1, default="~", help=HELP_path, metavar="path")
parser.add_argument("-d", "--depth", nargs=1, default=[0], type=int, help=HELP_dpth, metavar="num")
parser.add_argument("-a", "--access", choices=range(8), nargs=1, default=None, type=int, help=HELP_axes, metavar="0-7")
parser.add_argument("-v", "--version", action="store_true", help="show version and exit")

def find(kw, by="n", case=0, path="~", depth=0, access=None):
	"""
	ARGS    kw      list      search keywords
	        by      str       search by
	        case    int/bool  ignore case
	        path    str       root search path
	        depth   int       recursion amount
	        access  int       permissions filter

	RETURN  exit_code, data
	"""

	# Prevents a bajillion false positives
	assert type(kw) in (list, tuple, set) and all(type(x) == str for x in kw), "FooF: error: kw must be a string"

	import os

	# Path handling
	if path[0] == "~":
		path = os.path.expanduser("~") + path[1:]
	path = os.path.abspath(path)
	if not os.path.isdir(path):
		return 1, "FooF: error: argument -p/--path: no such directory " + path

	# Permissions
	if access is not None:
		def permissions(f):
			P = oct(os.stat(f).st_mode & 0o777)[-3:]
			own = os.geteuid() != os.stat(f).st_uid
			return int(P[own * 2])

	# Prepare content search
	if by in "ca":
		import re, shlex
		kw2 = "|".join(map(lambda k: re.escape(k).replace("'", r"\'"), kw))
		if not os.popen("which ag").read().strip():
			return 1, "Dependency required: ag\nGet it from (http://github.com/ggreer/the_silver_searcher)"

	matches = set()
	a = os.walk(path)
	for src, dirs, files in a:
		if depth and src.count("/") - path.count("/") >= depth:
			continue
		if by in "na":
			for name in dirs + files:
				for keyw in kw:
					N, K = (name.lower(), keyw.lower()) if case else (name, keyw)
					if K in N:
						matches.add(src + os.path.sep + name)
						break
		if by in "ca":
			cmd = f"ag --depth 1 -l -m 1 {('-s', '-i')[case]} '{kw2}' {shlex.quote(src)} 2>/dev/null"
			matches.update(x for x in os.popen(cmd).read().split("\n") if x)
	if access is not None:
		matches = filter(lambda f: permissions(f) == (access[0] if type(access) == list else access), matches)
	return 0, sorted(matches)

if __name__ == "__main__":
	try:
		args = parser.parse_args()
		if args.version:
			exit(f"Flags of our Fathers (FooF) v{v} ({d})")
		F = find(args.string, args.by, args.case, args.path[0], args.depth[0], args.access)
		if F[1]:
			print("\n".join(F[1]) if type(F[1]) == list else F[1])
	except KeyboardInterrupt:
		print()