#this is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1:", arg1, "arg2:", arg2)

#ok, thats *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
    print("arg1:", arg1, "arg2:", arg2)

def print_one(arg1):
    print("arg1", arg1)

def print_none():
    print("I got nothin")

print_two("brandon","norsworthy")
print_two_again("brandon","norsworthy")
print_one("first")
print_none