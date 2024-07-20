class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {')': '(', ']': '[', '}': '{'}
        stack = []
        for value in s:
            if value in my_dict.values():
                stack.append(value)
            else:
                try:
                    if stack[-1] != my_dict[value]:
                        return False
                except IndexError:
                    return False
                stack.pop()
        return True if not stack else False
