class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        res = []
        def dfs(idx, tmp_res):
            if idx == len(s):
                res.append(tmp_res[:-1])
            for i in range(idx+1, len(s)+1):
                if s[idx:i] in wordDict:
                    dfs(i, tmp_res+s[idx:i]+' ')
        dfs(0, '')
        return res