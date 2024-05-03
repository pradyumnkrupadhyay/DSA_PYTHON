class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        candidate1 = 0
        candidate2 = 1 
        count1 = 0
        count2 = 0
        
        for n in nums:
            
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1
                
        return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums)//3]
        