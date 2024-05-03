class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        required = len(counter)
        res = ""
        left = 0
        for right, char in enumerate(s, 1):
            if char not in counter:
                continue

            counter[char] -= 1
            if counter[char] == 0:
                required -= 1

            while required == 0 and left < right:
              
                char = s[left]
                if char in counter:
                    if not res or right - left < len(res):
                        res = s[left:right]

                    counter[char] += 1
                    if counter[char] == 1:
                        required += 1

                left += 1

        return res

