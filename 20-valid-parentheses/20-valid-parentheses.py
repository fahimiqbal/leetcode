class Solution:
    def isValid(self, s: str) -> bool:
        openParentheses = { '(': ')', '{': '}', '[': ']'}
        closeParentheses = {')': '(', '}': '{', ']': '['}
        stack = []
        for i, item in enumerate(s):
            if item in openParentheses.keys():
                stack.append(item)
            elif item in closeParentheses.keys() and len(stack) > 0 and item == openParentheses[stack[-1]]:
                stack.pop()
            else:
                return False

        if len(stack) == 0:
            return True

        return False