class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        lookup = set(nums)
        return max([x for x in lookup if x > 0 and -x in lookup] or [-1])