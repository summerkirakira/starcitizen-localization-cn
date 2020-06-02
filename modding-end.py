#!/usr/bin/python

import patcher

result = patcher.restore_game()
if result == 0:
    print("Already restored")
    input("")
    exit(0)
if result == 1:
    print("Done")
    input("")
    exit(0)
print("Error: can't restore. Please check file permission")
input("")
exit(1)
