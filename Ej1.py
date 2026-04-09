EPSILON = 'ε'

grammar = {
    'S': [['A', 'uno', 'B', 'C'], ['S', 'dos']],
    'A': [['B', 'C', 'D'], ['A', 'tres'], [EPSILON]],
    'B': [['D', 'cuatro', 'C', 'tres'], [EPSILON]],
    'C': [['cinco', 'D', 'B'], [EPSILON]],
    'D': [['seis'], [EPSILON]]
}

first = {nt: set() for nt in grammar}
follow = {nt: set() for nt in grammar}

# FIRST
changed = True
while changed:
    changed = False
    for nt in grammar:
        for prod in grammar[nt]:
            for symbol in prod:
                if symbol not in grammar:  # terminal
                    if symbol not in first[nt]:
                        first[nt].add(symbol)
                        changed = True
                    break
                else:
                    antes = len(first[nt])
                    first[nt] |= (first[symbol] - {EPSILON})
                    if EPSILON not in first[symbol]:
                        break
                    if len(first[nt]) > antes:
                        changed = True
            else:
                if EPSILON not in first[nt]:
                    first[nt].add(EPSILON)
                    changed = True

# FOLLOW
follow['S'].add('$')

changed = True
while changed:
    changed = False
    for nt in grammar:
        for prod in grammar[nt]:
            temp = follow[nt].copy()
            for symbol in reversed(prod):
                if symbol in grammar:
                    antes = len(follow[symbol])
                    follow[symbol] |= temp
                    if EPSILON in first[symbol]:
                        temp |= (first[symbol] - {EPSILON})
                    else:
                        temp = first[symbol]
                    if len(follow[symbol]) > antes:
                        changed = True
                else:
                    temp = {symbol}

# PREDICT
predict = {}
for nt in grammar:
    for prod in grammar[nt]:
        key = f"{nt} -> {' '.join(prod)}"
        predict[key] = set()

        for symbol in prod:
            if symbol not in grammar:
                predict[key].add(symbol)
                break
            else:
                predict[key] |= (first[symbol] - {EPSILON})
                if EPSILON not in first[symbol]:
                    break
        else:
            predict[key] |= follow[nt]

# PRINT
print("FIRST:", first)
print("FOLLOW:", follow)
print("PREDICT:", predict)