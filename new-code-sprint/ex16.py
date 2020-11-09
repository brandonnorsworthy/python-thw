from sys import argv

script, filename = argv

print("Were going to erase %r" % filename)
print("If you dont want that hit CTRL-C")
print("If you do want that hit ENTER")

input("?")

print("Opening the file")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target = open(filename, 'w')

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("im going to write these to the file")

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print("and finally, we close it")
target.close