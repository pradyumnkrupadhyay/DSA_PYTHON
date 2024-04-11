class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        remain = len(num) - k
        for dig in num:
            while k and stack and stack[-1] > dig:
                stack.pop()
                k -= 1
            stack.append(dig)
        return ''.join(stack[:remain]).lstrip('0') or '0'