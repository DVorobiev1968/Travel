# -*- coding: utf-8 -*-

import codecs
import getopt
import sys

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "")
        if len(args) > 2:
            raise getopt.error("Too many arguments.")
        if len(args) < 2:
            raise getopt.error("Too few arguments.")
    except getopt.error as msg:
        usage(msg)
    try:
        src = args[0]
        dst = args[1]
        source = codecs.open(src, "rb").read().decode('unicode-escape')
        codecs.open(dst, "wb", "utf-8").write(source)
    except ValueError as msg:
        usage(msg)
    module = sys.argv[0].split('/')[-1].split('.')[0]
    sys_info = "{0} convert to file: {1}".format(module, args[1])
    print (sys_info)

"""
=====================
Create dump
=====================
Usage:
dumpdata.py <input> <output>
"""
def usage(msg=None):
    sys.stdout = sys.stderr
    if msg:
        print(msg)
    print("\n", __doc__)
    sys.exit(2)


if __name__ == '__main__':
    try:
        main()
    except getopt.error as msg:
        usage(msg)
