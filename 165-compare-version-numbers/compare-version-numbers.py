class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = version1.split('.')
        l2 = version2.split('.')
        max_length = max(len(l1), len(l2))
        
        i = 0
        while i < max_length:
            
            if i < len(l1):
                num1 = int(l1[i])
            else:
                num1 = 0
                
            if i < len(l2):
                num2 = int(l2[i])
            else:
                num2 = 0   
                
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
            
            i += 1
        return 0
        