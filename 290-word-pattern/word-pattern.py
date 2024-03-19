class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        hash_pattern = {}
        hash_words = {}

        for i in range(len(pattern)):
            if pattern[i] in hash_pattern:
                if hash_pattern[pattern[i]] != words[i]:
                    return False
            else:
                hash_pattern[pattern[i]] = words[i]

            if words[i] in hash_words:
                if hash_words[words[i]] != pattern[i]:
                    return False
            else:
                hash_words[words[i]] = pattern[i]

        return True

        