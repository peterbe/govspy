elements = {}
elements["H"] = 1
print elements["H"]  # 1

# remove by key
elements["O"] = 8
elements.pop("O")

# do something depending on the being there
if "O" in elements:
    print elements["O"]
if "H" in elements:
    print elements["H"]
