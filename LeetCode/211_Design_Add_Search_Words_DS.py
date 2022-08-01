'''
211. Design Add and Search Words Data Structure
Medium

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:
WordDictionary() Initializes the object.

void addWord(word) Adds word to the data structure, it can be matched later.

bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. 
word may contain dots '.' where dots can be matched with any letter. 

Example:
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:
1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 3 dots in word for search queries.
At most 10^4 calls will be made to addWord and search.
'''
class TrieNode:
    def __init__(self, charecter):
        self.charecter = charecter
        self.is_end = False
        self.children = dict()
        self.counter = 0

class WordDictionary:
    def __init__(self):
        self.root = TrieNode('*')

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        
        node.is_end = True
        node.counter += 1


    def search(self, word: str, node= None) -> bool:
        if node == None:
            node = self.root
        if len(word) == 0:
            return node.is_end
        if word[0] != '.' and word[0] not in node.children:
            return False
        elif word[0] == '.':
            if len(node.children.keys()) == 0:
                return False
            for children in node.children.keys():
                if not self.search(word[1:], node.children[children]):
                    return False
        elif len(word) > 0:
            return self.search(word[1:], node.children[word[0]])
        
        return True

wordDictionary = WordDictionary()
print(wordDictionary.addWord("bad"))
print(wordDictionary.addWord("dad"))
print(wordDictionary.addWord("mad"))
print(wordDictionary.search("pad")) # return False
print(wordDictionary.search("bad")) # return True
print(wordDictionary.search(".ad")) # return True
print(wordDictionary.search("b..")) # return True

'''
["WordDictionary","addWord","addWord","search","search","search","search","search","search"]
[[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]]
[null,null,null,true,true,false,true,false,false]
'''
wordDictionary = WordDictionary()
print(wordDictionary.addWord("at")) #None
print(wordDictionary.addWord("and")) #None
print(wordDictionary.addWord("an")) #None
print(wordDictionary.addWord("add")) #None
print(wordDictionary.search("a")) #False
print(wordDictionary.search(".at")) #False