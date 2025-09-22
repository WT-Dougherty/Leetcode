"""
Problem: Valid Parentheses (Stack)
----------------------------------
Given a string s containing only '()[]{}', determine if the input string is valid.

Rules:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

Approach:
- Use a stack; push opening, on closing check top matches.

Time: O(n) | Space: O(n)
"""
def is_valid(s: str) -> bool:
    pairs = {')':'(', ']':'[', '}':'{'}
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs.get(ch, None):
                return False
            stack.pop()
    return not stack

def _test():
    assert is_valid("()")
    assert is_valid("()[]{}")
    assert not is_valid("(]")
    assert not is_valid("([)]")
    assert is_valid("{[]}")

if __name__ == "__main__":
    _test()
    print("OK")