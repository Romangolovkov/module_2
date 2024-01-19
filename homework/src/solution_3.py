def bracket_balance(brackets: str) -> bool:
    brackets = [bracket for bracket in brackets]
    for i in range(len(brackets) - 2, -1, -1):
        if (brackets[i] == '(' and brackets[i + 1] == ')') \
        or (brackets[i] == '[' and brackets[i + 1] == ']') \
        or (brackets[i] == '{' and brackets[i + 1] == '}'):
            brackets.pop(i)
            brackets.pop(i)
    return bool(not(brackets))


print(bracket_balance('[(])'))
print(bracket_balance('}'))
print(bracket_balance('[]['))
print(bracket_balance(')('))
print(bracket_balance('{([]){}}'))
print(bracket_balance('{([]){}}['))