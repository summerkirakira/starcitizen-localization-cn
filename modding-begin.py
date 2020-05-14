#!/usr/bin/python

import patcher

result = patcher.patch_game()
if result == 0:
    print "Already patched"
    raw_input()
    exit(0)
if result == 1:
    print "Done"
    raw_input()
    exit(0)
if result == -1:
    print "Error: can't patch. Please update patcher"
else:
    print "Error: can't patch. Please check file permission"
raw_input()
exit(1)



       



