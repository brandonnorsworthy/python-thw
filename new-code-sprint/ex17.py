from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from", from_file, " to", to_file)

in_file = open(from_file)
indata = in_file.read()

print("The input file is", len(indata), "bytes long")

print("Does the output file exist?", exists(to_file))
print("Read, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done")

out_file.close()
in_file.close()