#Class
# class User(object):
#     pass

# michael = User()
# anna = User()

# print michael, anna

#Self and __init__()
class User(object):
    name = "Anna"
anna = User()
print "anna's name:", anna.name
User.name = "Bob"
print "anna's name after change:", anna.name
bob = User()
print "bob's name:", bob.name


