# get the current script path.
import os
here = os.path.dirname(os.path.realpath(__file__))
subdir = "rating-output"
filename = "myfile2.txt"
filepath = os.path.join(here, subdir, filename)

# create your subdirectory
#os.mkdir(os.path.join(here, subdir))

# create an empty file.
try:
    f = open(filepath, 'w')
    f.close()
except IOError:
    print("Wrong path provided")