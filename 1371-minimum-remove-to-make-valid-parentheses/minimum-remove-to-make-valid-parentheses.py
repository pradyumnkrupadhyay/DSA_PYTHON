class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result = list(s)
        count = 0
        for i, v in enumerate(result):
            if v == '(':
                count += 1
            elif v == ')':
                if count:
                    count -= 1
                else:
                    result[i] = ""
        if count:
            for i in reversed(range(len(result))):
                if result[i] == '(':
                    result[i] = ""
                    count -= 1
                    if not count:
                        break
        return "".join(result)
        