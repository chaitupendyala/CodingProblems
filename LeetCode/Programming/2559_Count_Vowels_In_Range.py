class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def startEndVowel(s):
            if len(s) == 0:
                return False
            elif s[0] in ('a', 'e', 'i', 'o', 'u') and s[-1] in ('a', 'e', 'i', 'o', 'u'):
                return True
            else:
                return False
        
        number_of_start = [0]
        for i in range(len(words)):
            if startEndVowel(words[i]):
                number_of_start.append(number_of_start[-1] + 1)
            else:
                number_of_start.append(number_of_start[-1])
        
        result = []
        for query in queries:
            result.append(number_of_start[query[1]+1] - number_of_start[query[0]])
        return result