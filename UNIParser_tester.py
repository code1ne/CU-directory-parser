import MLStripper
import urllib
import UNIParser

def strip_last_word(s):
	words = s.split(" ")
	del words[-1]
	return " ".join(words)

dir_info = urllib.urlopen("https://directory.columbia.edu/people/uni?code=aar2153").read()
dir_info = MLStripper.strip_tags(dir_info)
# dir_info = dir_info.split(":")
# dir_info = dir_info[1::]

# name = dir_info[0].split()
# name = name[name.index("Page")+1:-1]
# dir_info[0] = " ".join(name)

# del dir_info[2]
# del dir_info[-1]

# for x in range(2, len(dir_info)):
# 	dir_info[x] = strip_last_word(dir_info[x])

print dir_info

print UNIParser.get_student_info("mc3415")

for x in range(10, -1):
	print x
