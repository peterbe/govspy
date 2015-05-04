initials = {}
for name in ('peter', 'anders', 'bengt', 'bengtsson'):
    initial = name[0]
    # if initial not in initials:
    #     initials[initial] = 0
    initials.setdefault(initial, 0)
    initials[initial] += 1
print initials
# outputs
# {'a': 1, 'p': 1, 'b': 2}
