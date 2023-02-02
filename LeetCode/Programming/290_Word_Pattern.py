class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern) and len(set(pattern)) != len(set(words)):
            return False
        mapping = {}
        for i in range(len(pattern)):
            if pattern[i] in mapping and mapping[pattern[i]] != words[i]:
                return False
            mapping[pattern[i]] = words[i]
        return True