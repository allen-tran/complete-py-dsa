from typing import Optional


class TrieNode:
    def __init__(self):
        self._children = {}
        self._is_terminal = False

    @property
    def children(self) -> dict:
        return self._children

    @property
    def is_terminal(self) -> bool:
        return self._is_terminal

    @is_terminal.setter
    def is_terminal(self, terminal) -> None:
        self._is_terminal = terminal


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, string: str) -> None:
        curr = self.root

        for character in string:
            if character not in curr.children:
                curr.children[character] = TrieNode()
            curr = curr.children[character]
        curr.is_terminal = True

    def search(self, string):
        curr = self.root

        for character in string:
            if character not in curr.children:
                return False
            curr = curr.children[character]

        return curr.is_terminal

    def starts_with(self, prefix: str) -> bool:
        curr = self.root

        for character in prefix:
            if character not in curr.children:
                return False
            curr = curr[character]

        return True

    def delete(self, string: str) -> None:
        def _delete(root: Optional[TrieNode], string: str, depth: int) -> Optional[TrieNode]:
            if root is None:
                return None

            if depth == len(string):

                if root.terminal:
                    root.terminal = False

                if len(root) == 0:
                    return None

                return root

            root.children[string[depth]] = _delete(root.children[string[depth]],
                                                   string, depth + 1)
            if len(root) == 0 and not root.terminal:
                root = None

            return root

    def is_empty(self) -> bool:
        return not self.root.children


if __name__ == "__main__":
    trie = Trie()
    trie.insert('HELLO')
    print(trie.search('HELLO'))
    print(trie.is_empty())
    trie.delete("HELLO")
    print(trie.search('HELLO'))
    print(trie.is_empty())
