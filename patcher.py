#!/usr/bin/python

import os
import mmap
import shutil
import platform

exe_file_path = 'Bin64/StarCitizen.exe'
game_file_path = 'Bin64/CIGDevelopmentTools.dll'
orig_signature = b'\xFE\x05\x48\x8B\x74\x24\x38\xB0\x01\x48\x83\xC4\x20\x5F\xC3'
patch_signature = b'\xFE\x05\x48\x8B\x74\x24\x38\xB0\x01\x90\x90\x90\x90\x90\x90'

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
    except Exception as e:
        return -2
    finally:
        mm.close()


def patch_game_exe():
    with open(exe_file_path, "r+b") as fp:
        return patch_file(fp, orig_signature, patch_signature)


def restore_game_exe():
    with open(exe_file_path, "r+b") as fp:
        return patch_file(fp, patch_signature, orig_signature)


def patch_game():
	if platform.release() == '7':
		print('Patch executable bug for Windows 7')
		result = patch_game_exe()
		if (result < 0):
			return result
	try:
		shutil.copyfile("patcher.bin", game_file_path)
		return 1;
	except Exception as e:
		print(e)
		return -1


def restore_game():
	if platform.release() == '7':
		print('Restore executable for Windows 7')
		restore_game_exe()
	try:
		if os.path.exists(game_file_path):
			os.remove(game_file_path)
			return 1
		else:
			return 0
	except Exception as e:
		print(e)
		return -1


