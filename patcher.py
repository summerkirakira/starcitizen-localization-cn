#!/usr/bin/python

import mmap

orig_signature = '\x40\x32\xF6\x80\xBF\xEE\x01'
patch_signature = '\x90\x90\x90\x80\xBF\xEE\x01'
game_file_path = 'Bin64/StarCitizen.exe'

def patch_file(fp, searchSig, patchSig):
    mm = mmap.mmap(fp.fileno(), 0)
    try:
        offset = mm.find(searchSig)
        if offset != -1:
            mm.seek(offset)
            mm.write(patchSig)
            return 1
        if mm.find(patchSig) != -1:
            return 0
        else:
            return -1
    except:
        return -2
    finally:
        mm.close()

def patch_game():
    with open(game_file_path, "r+b") as fp:
        return patch_file(fp, orig_signature, patch_signature)


def restore_game():
    with open(game_file_path, "r+b") as fp:
        return patch_file(fp, patch_signature, orig_signature)



       



