#!/usr/bin/python

import patcher

result = patcher.restore_game()
if result == 0:
    print "Already restored"
    raw_input()
    exit(0)
if result == 1:
    print "Done"
    raw_input()
    exit(0)
if result == -1:
    print "Error: can't restore. Please update patcher"
else:
    print "Error: can't restore. Please check file permission"
raw_input()
exit(1)



       



