import UNIParser

# example usage
# puts student information in JSOn

# UNI file not included for privacy reasons
UNIs = open("small_UNI_list.txt", "r")
UNI_json = []
for line in UNIs:
	UNI_json.append(UNIParser.get_student_info(line))
print UNI_json