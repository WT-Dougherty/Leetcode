"""
Problem: Valid Parentheses
----------------------------------
Given a string s containing only '()[]{}', determine if the input string is valid.

Rules:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

Approach: Create a Stack
- The stack will begin empty, and open parentheses will be pushed to the stack.
- There will be a lookup hash map, where the keys are the closing brackets and the values are the opening brackets
- There will also be a set containing the three opening brackets. This will be used to check if the new character should be added to the stack.

Three input cases:
Opening bracket -> add to stack
Closing bracket -> check if map[char] == stack.pop() ? continue : return False
Other character -> return False

"""

from queue import Empty


def is_valid(s: str) -> bool:
    stack = []
    lookup = {")": "(", "}": "{", "]": "["}
    stack_sigma = {"(", "[", "{"}

    for c in s:
        if c in stack_sigma:
            stack.append(c)
        elif c in lookup.keys():
            if stack.pop() == lookup[c]:
                continue
            else:
                return False
        else:
            return False
    if stack == []:
        return True
    return False


def _test():
    assert is_valid("()")
    assert is_valid("()[]{}")
    assert not is_valid("(]")
    assert not is_valid("g{}[]")
    assert not is_valid("([)]")
    assert is_valid("{[]}")


if __name__ == "__main__":
    _test()
    print("OK")
