#!/usr/bin/env python
# encoding: utf-8

import os

#no os.walk().

if __name__ == "__main__":
    SIG = {
        ".git":"git pull",
        ".hg":"hg pull",
        ".svn":"svn update",
    }
    curdir_abs = os.path.dirname(os.path.abspath(__file__))
    files_and_dirs__abs = os.listdir(curdir_abs + os.sep)
    for o in files_and_dirs__abs:
        if os.path.isdir(o):
            os.chdir(o)
            for k in SIG:
                if os.path.exists(k):
                    print "Found %s in %s" % (k,o)
                    print "Updating..."
                    os.system(SIG[k])
            os.chdir(os.pardir)
