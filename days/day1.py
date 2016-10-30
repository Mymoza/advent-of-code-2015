""" BASIC INSTRUCTIONS """
# ( go up one floor
# ) go down one floor

""" SOME HELP """
# (()) and ()() both result in floor 0
# ((( and (()(()( both result in floor 3
# ))(((( result in floor 3
# ()) and ))( result in floor -1 (first basement level)
# ))) and )())()) both result in floor -3

""" SO THE FLOORS ARE : """
# ...
# -3
# -2
# -1
# 0
# 1
# 2
# ...

import os
os.chdir("../resources") # Change the current directory
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory

file_day1 = open("day1", "r")


where_is_santa = 0

with file_day1 as f:
  while True:
    c = f.read(1)
    if not c:
      print "End of file"
      break
    if c == "(":
        where_is_santa = where_is_santa +1
    elif ")" == c:
        where_is_santa = where_is_santa - 1

file_day1.close()

print "santa is at floor", where_is_santa