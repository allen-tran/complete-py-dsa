class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_terminal = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, string):
        pass

    def search(self, string):
        pass

    def delete(self, string):
        pass

    def contains(self, string):
        pass

    def is_empty(self):
        return not self.root.children


if __name__ == "__main__":
    root = TrieNode(5)
