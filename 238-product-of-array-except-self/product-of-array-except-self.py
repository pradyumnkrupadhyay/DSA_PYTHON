class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        inputLength = len(nums)
        left=1

        for i in range(inputLength):
            output.append(left)
            left *= nums[i]

        right=1
        for i in range(inputLength-1,-1,-1):
            output[i] *=right
            right *= nums[i]
        return output