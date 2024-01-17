def bracket_balance(brackets: str) -> bool:
    brackets = [bracket for bracket in brackets]
    if len(brackets) % 2 != 0:
        return False
    else:
        for i in range(len(brackets) // 2):
            if (brackets[0] == '(' and brackets[-1] == ')') \
            or ((brackets[0] == '[' and brackets[-1] == ']')) \
            or ((brackets[0] == '{' and brackets[-1] == '}')):
                brackets.pop(0)
                brackets.pop(-1)
            else:
                return False
                break
        return True


print(bracket_balance('[(])'))
print(bracket_balance('}'))
print(bracket_balance('[]['))
print(bracket_balance(')('))
print(bracket_balance('{([])}'))