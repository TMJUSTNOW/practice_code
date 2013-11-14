def zero(s):
    if s[0] == "0":
        return s[1:]


def one(s):
    if s[0] == "1":
        return s[1:]

"""
def rule_sequence(s, rules):
    for rule in rules:
        s = rule(s)
        if s == None:
            break

    return s
"""


def rule_sequence(s, rules):
    if s is None:
        return None
    if len(rules) == 0:
        return s
    return rule_sequence(rules[0](s), rules[1:])


print rule_sequence('0101', [zero, one, zero])
# => 1

print rule_sequence('0101', [zero, zero])
# => None

# Reimplement rule_sequence as a recursive function.
# Make sure that when it is run, it returns the results shown above.
