#!/usr/bin/python

import os
import shutil

game_file_path = 'Bin64/dbghelp.dll'


def patch_game():
	try:
		shutil.copyfile("patcher.bin", game_file_path)
		return 1;
	except Exception as e:
		print(e)
		return -1


def restore_game():
	try:
		if os.path.exists(game_file_path):
			os.remove(game_file_path)
			return 1
		else:
			return 0
	except Exception as e:
		print(e)
		return -1
