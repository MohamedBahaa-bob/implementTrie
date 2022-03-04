# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# correct solution for the leetCode Q, however it defies the purpose of a prefix Tree (startsWith in O(1))
"""class TrieNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def compareStrings(word1, word2):
    i = 0
    while i in range(len(word1)) and i in range(len(word2)):
        if word1[i] > word2[i]:
            return 1
        elif word1[i] < word2[i]:
            return -1
        else:
            i += 1
    if len(word1) == len(word2):
        return 0
    elif len(word1) < len(word2):
        return 1
    return -1

def prefixOf(word1, word2):
    i = 0
    if len(word1) < len(word2):
        return False
    while i in range(len(word2)):
        if word1[i] == word2[i]:
            i += 1
        else:
            return False
    return True

class Trie:

    def __init__(self):
        self.root = None

    def insert(self, word: str) -> None:
        if not self.root:
            self.root = TrieNode(word)
            return
        current = self.root
        while current:
            compres = compareStrings(current.val, word)
            if compres > 0:
                last = current
                current = current.left
                left = True
            elif compres < 0:
                last = current
                current = current.right
                left = False
            else:
                return
        if left:
            last.left = TrieNode(word)
        else:
            last.right = TrieNode(word)


    def search(self, word: str) -> bool:
        if not self.root:
            return False
        if not word:
            return True
        current = self.root
        while  current:
            compres = compareStrings(current.val, word)
            if compres > 0:
                current = current.left
            elif compres < 0:
                current = current.right
            else:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        if not self.root:
            return False
        if not prefix:
            return True
        current = self.root
        while current:
            compres = compareStrings(current.val, prefix)
            if prefixOf(current.val, prefix):
                return True
            elif compres > 0:
                current = current.left
            elif compres < 0:
                current = current.right
            else:
                print("error")
        return False"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.endOfWord = True

    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if c not in current.children:
                return False
            else:
                current = current.children[c]
        return current.endOfWord

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if c not in current.children:
                return False
            else:
                current = current.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
