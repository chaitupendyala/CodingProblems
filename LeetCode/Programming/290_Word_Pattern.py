class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        matching = {}
        reverse_matching = {}
        for i in range(len(pattern)):
            print(pattern[i], words[i])
            print(matching, reverse_matching)
            if pattern[i] not in matching and words[i] not in reverse_matching:
                matching[pattern[i]] = words[i]
                reverse_matching[words[i]] = pattern[i]
            elif pattern[i] in matching and words[i] in reverse_matching and matching[pattern[i]] == words[i] and reverse_matching[words[i]] == pattern[i]:
                continue
            else:
                return False
        return True