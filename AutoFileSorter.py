import os
import ctypes
import json
import time
import pathlib

#Loads all the file formats from fileformats.json
with open("fileformats.json", 'r') as f:
    formats = json.load(f)

audioformats = formats[0]
videoformats = formats[1]
textformats = formats[2]
imageformats = formats[3]

#New file format question and addition
if ctypes.windll.user32.MessageBoxW(0, "Do you want to add a new file format?", "New file format?", 4) == 6:
	newformat = input("Please enter the file format name (Ex: if your format is .mp4 enter mp4)")
	newformatcategory = input("And in what category do you want to add this format in? (Choice: Audio, Video, Text, Image)").lower()

	#Adds the new format
	if newformatcategory == "audio":
		audioformats.append(newformat)
	elif newformatcategory == "video":
		videoformats.append(newformat)
	elif newformatcategory == "text":
		textformats.append(newformat)
	elif newformatcategory == "image":
		imageformats.append(newformat)

	formats = []

	formats.append(audioformats)
	formats.append(videoformats)
	formats.append(textformats)
	formats.append(imageformats)

	#Reupdates fileformats.json
	with open("fileformats.json", 'w') as f:
		json.dump(formats, f)
#Reset fileformats.json to default question
else:
	if ctypes.windll.user32.MessageBoxW(0, "Do you want to reset fileformats.json to Default?", "Reset to Default?", 4) == 6:
		if ctypes.windll.user32.MessageBoxW(0, "Are you sure? You cannot undo this part", "Are you sure?", 4) == 6:
			formats = [['aa', 'aac', 'aax', 'm4a', 'mmf', 'mp3', 'ogg', 'wav', 'wma', 'webm'], ['mp4', 'avi','mov', 'flv', 'ts', 'mk4'], ['txt', 'doc', 'docx', 'odt', 'pdf', 'rtf', 'tex', 'wpd'], ['tif', 'tiff', 'bmp', 'jpg', 'jpeg', 'gif', 'png', 'eps', 'raw', 'cr2', 'nef', 'orf', 'sr2']]

			with open('fileformats.json', 'w') as f:
				json.dump(formats, f)
			ctypes.windll.user32.MessageBoxW(0, "Done! fileformats.json has been reset to default", "Done", 0)

#Path for the unsorted/input folder
unsortedfolderpath = input("Please input the path of the unsorted folder. (Or enter default to stick to the default path)")
if unsortedfolderpath == "default" or unsortedfolderpath == "Default":
	unsortedfolderpath = "unsorted"

#Path for the sorted/output folder
sortedfolderpath = input("Please input the path of the output folder. (Or enter default to stick to the default path)")
if sortedfolderpath == "default" or sortedfolderpath =="Default":
	sortedfolderpath = "sorted"

#Checks if input and output folders exists and creates them if not
if pathlib.Path(unsortedfolderpath).exists() == False:
	os.mkdir(unsortedfolderpath)
elif pathlib.Path(sortedfolderpath).exists() == False:
	os.mkdir(sortedfolderpath)

#Checks if the category folders are there and makes them if not
if pathlib.Path(f"{sortedfolderpath}\\text").exists() == False:
	os.mkdir(f"{sortedfolderpath}\\text")
if pathlib.Path(f"{sortedfolderpath}\\video").exists() == False:
	os.mkdir(f"{sortedfolderpath}\\video")
if pathlib.Path(f"{sortedfolderpath}\\images").exists() == False:
	os.mkdir(f"{sortedfolderpath}\\images")
if pathlib.Path(f"{sortedfolderpath}\\audio").exists() == False:
	os.mkdir(f"{sortedfolderpath}\\audio")
if pathlib.Path(f"{sortedfolderpath}\\other").exists() == False:
	os.mkdir(f"{sortedfolderpath}\\other")

with open("fileformats.json", 'r') as f:
    formats = json.load(f)

audioformats = formats[0]
videoformats = formats[1]
textformats = formats[2]
imageformats = formats[3]

if len(os.listdir(unsortedfolderpath)) == 0:
	if ctypes.windll.user32.MessageBoxW(0, "Input folder is empty", "", 0) == 1:
		exit()

for file in os.listdir(unsortedfolderpath):
	fileformat = file.split(".")[-1]
	if fileformat in textformats:
		os.rename(f"{unsortedfolderpath}\\{file}", f"{sortedfolderpath}\\text\\{file}")
	elif fileformat in videoformats:
		os.rename(f"{unsortedfolderpath}\\{file}", f"{sortedfolderpath}\\video\\{file}")
	elif fileformat in imageformats:
		os.rename(f"{unsortedfolderpath}\\{file}", f"{sortedfolderpath}\\images\\{file}")
	elif fileformat in audioformats:
		os.rename(f"{unsortedfolderpath}\\{file}", f"{sortedfolderpath}\\audio\\{file}")
	else:
		os.rename(f"{unsortedfolderpath}\\{file}", f"{sortedfolderpath}\\other\\{file}")