class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen={}
        if(max(nums)<1):
            return 1
        for ele in nums:
            seen[ele]=True

        for i in range(1,len(nums)+2): 
            if(i not in seen):
                return i 


        