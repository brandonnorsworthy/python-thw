from sys import argv

script, user_name = argv
prompt = '> '

print("Hi ", user_name, "I'm the ", script, " script.")
print("Id like to ask a few questions")
print("Do you like me", user_name)
likes = input(prompt)

print("where do you live")
lives = input(prompt)

print("""
Alright so you said %r about liking me
And you live in %r
""" % (likes, lives))