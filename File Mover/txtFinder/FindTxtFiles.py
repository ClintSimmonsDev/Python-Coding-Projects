import os
import datetime

file_list = []
for file in os.listdir("C:\\Users\Silverfox Studios\myProjects\Python Projects\Tech-Academy-Python-Coding-Projects\Iterable Files Drill"):
    if file.endswith(".txt"):
        file_list.append(file)
time = str(os.path.getmtime("C:\\Users\Silverfox Studios\myProjects\Python Projects\Tech-Academy-Python-Coding-Projects\Iterable Files Drill"))
joined_file = os.path.join("C:\\Users\Silverfox Studios\myProjects\Python Projects\Tech-Academy-Python-Coding-Projects\Iterable Files Drill, file")

print("\n")

for file in file_list:
    print(file)
    print("Last Modified Time: " + time)
    print("~~~~~~~~~~~~~")