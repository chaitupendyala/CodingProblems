class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def makeTrie(words):
            _end = "_end_"
            root = dict()
            for word in words:
                current_dict = root
                for letter in word:
                    current_dict = current_dict.setdefault(letter, {})
                current_dict[_end] = _end
            return root
        trie = makeTrie(strs)
        longest = ""
        while trie:
            list_of_keys = list(trie.keys())
            if len(list_of_keys) == 1:
                if list_of_keys[0] != "_end_":
                    current = list_of_keys[0]
                    longest += current
                    trie = trie[current]
                else:
                    break
            else:
                break
        return longest