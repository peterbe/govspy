symbol = raw_input()
if symbol == "O":
    print "Oxygen"
elif symbol == "H":
    print "Hydrogen"
elif symbol == "He":
    print "Helium"
elif symbol == "Na":
    print "Sodium"
else:
    print "I have no idea what %s is" % symbol


# Alternative solution
symbol = raw_input()
db = {
    "H": "Hydrogen",
    "He": "Helium",
    "O": "Oxygen",
    "Na": "Sodium",
}
print db.get(symbol, "I have no idea what %s is" % symbol)
