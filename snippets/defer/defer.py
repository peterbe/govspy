f = open("defer.py")
try:
    f.read()
finally:
    f.close()
