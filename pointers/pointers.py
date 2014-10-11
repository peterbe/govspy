# There is no equivalent to pointers in python

def upit(str):
    return str.upper()


def uplist(mylist):
    for i in range(len(mylist)):
        mylist[i] = mylist[i].upper()

name = "peter"
upit(name)
print name  # peter
name = upit(name)
print name  # PETER

# but you can do a useless cheat and make it mutable
name = list("peter")
uplist(name)
name = ''.join(name)
print name  # PETER
