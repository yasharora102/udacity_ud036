from __future__ import print_function
import os

# get the files 

def rename_files():
	file_list = os.listdir(r"/home/stealthflame/version-control/udacity_ud036/rename_files/prank")
	print(file_list)

	saved_path = os.getcwd()
	print("The Current Working Directory is" , saved_path)
	os.chdir(r'/home/stealthflame/version-control/udacity_ud036/rename_files/prank')

	# rename the files
	for file_name in file_list:
		os.rename(file_name,file_name.translate(None,'0123456789'))

	os.chdir(saved_path)







rename_files()