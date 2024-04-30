class Solution:
    def wonderfulSubstrings(self, word: str) -> int:

        freq = Counter([0])
        mask, ans = 0, 0
        
        for ch in word:
            idx = ord(ch) - ord("a")
            mask ^= (1 << idx)
            if mask in freq:
                ans += freq[mask]
            for i in range(10):
                mask_pre = mask ^ (1 << i)
                if (mask_pre := mask ^ (1 << i)) in freq:
                    ans += freq[mask_pre]
            freq[mask] += 1
        
        return ans