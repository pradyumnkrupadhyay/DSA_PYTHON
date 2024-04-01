class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # length = 0
        # for i in reversed(s):
        #     if i == ' ':
        #         if length:
        #             break
        #     else:
        #         length += 1
        # return length 

        return len(s.strip().split(" ")[-1])