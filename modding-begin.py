#!/usr/bin/python

import patcher

result = patcher.patch_game()
if result == 0:
    print("Already patched")
    input("")
    exit(0)
if result == 1:
    print("Done")
    input("")
    exit(0)
print("Error: can't patch. Please check file permission")
input("")
exit(1)
