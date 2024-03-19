class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        res = 0
        count = 0
        nums.sort()
        for i in range(length):
            if i == 0:
                count += 1
            else:
                if nums[i] == nums[i-1]:
                    continue
                elif nums[i] != nums[i-1]+1:
                    count = 1
                else:
                    count += 1
            res = max(res, count)
        return res