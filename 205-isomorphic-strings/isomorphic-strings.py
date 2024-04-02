class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st_dict = {}
        ts_dict = {}
        for c1, c2 in zip(s, t):
            if c1 in st_dict:
                if st_dict[c1] != c2:
                    return False
            else:
                if c2 in ts_dict:
                    return False
                else:
                    st_dict[c1] = c2
                    ts_dict[c2] = c1
        return True
        