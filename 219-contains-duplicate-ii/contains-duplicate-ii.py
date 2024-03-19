class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lookup = {}
        for i, num in enumerate(nums):
            if num not in lookup:
                lookup[num] = i
            else:
                # It the value occurs before, check the difference.
                if i - lookup[num] <= k:
                    return True
                # Update the index of the value.
                lookup[num] = i
        return False
        