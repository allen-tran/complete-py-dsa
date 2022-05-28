from __future__ import annotations
from typing import Any


class IndexOutOfRangeException(Exception):
    def __init__(self) -> None:
        super().__init__("Index out of range!")


class EmptyListException(Exception):
    def __init__(self) -> None:
        super().__init__("Attempted to remove or retrieve data from an empty list!")


class Node:
    def __init__(self, val, next=None) -> None:
        """value and next initialization

        Args:
            val (Generic): value
            next (Generic, optional): next pointer. Defaults to None.
        """
        self._val = val
        self._next = next

    @property
    def val(self) -> Any:
        """getter for data

        Returns:
            Any: value
        """
        return self._val

    @property
    def next(self) -> Node:
        """getter for next pointer

        Returns:
            Node: next node pointer
        """
        return self._next

    @val.setter
    def val(self, val) -> None:
        self._val = val

    @next.setter
    def next(self, next) -> None:
        self._next = next


class LinkedList:
    def __init__(self) -> None:
        """constructor for LL initialization
        """
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, val) -> None:
        """O(1) operation to put node at end

        Args:
            val (any): value of node to create
        """
        node = Node(val)
        if self._size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1

    def prepend(self, val) -> None:
        node = Node(val)

        if self._size == 0:
            self.head = node
            self.tail = node
            self._size += 1
        else:
            node.next = self.head
            self.head = node

    def insert_after(self, val, position) -> None:
        node = Node(val)
        if self.__check_position(position):
            curr = self.head
            i = 0
            while i != position:
                curr = curr.next
                i += 1
            node.next = curr.next
            curr.next = node

    def insert_before(self, val, position) -> None:
        node = Node(val)

        if position == 0:
            self.preprend(val)
            return None

        if self.__check_position(position):
            curr = self.head
            i = 0

            while i != position - 1:
                curr = curr.next
                i += 1
            node.next = curr.next
            curr.next = node

    def pop_front(self) -> any:
        if self._size == 0:
            return "There is nothing to pop :("
        else:
            curr = self.head
            temp = curr.val
            curr = curr.next
            self.head = curr

            if not self.head:
                self.tail = None
            self._size -= 1
            return temp

    def pop_end(self) -> any:
        if self._size == 0:
            return "There is nothing to pop :("
        elif self._size == 1:
            temp = self.head.val
            self.head = None
            self.tail = None
            return temp
        else:
            temp = self.tail.val
            curr = self.head
            for _ in range(self._size - 1):
                curr = curr.next
            curr.next = None
            self.tail = curr
            return temp

    def remove_at(self, position) -> any:
        if self.__check_position(position):
            if position == 0:
                return self.pop_front()

            curr = self.head
            for _ in range(position-1):
                curr = curr.next
            temp = curr.next
            curr.next = curr.next.next
            self._size -= 1
            return temp

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __check_position(self, pos: int) -> bool:
        """check if a position is correct
        Args:
            pos (int): the position to be checked
        Raises:
            IndexOutOfRangeException: raised when the position is out of range
        """
        if pos < 0 or pos >= self._size:
            raise IndexOutOfRangeException()
        return True

    @property
    def size(self) -> int:
        return self._size

    @property
    def empty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size

    def __bool__(self) -> bool:
        return self._size != 0

    def __iter__(self):
        self._current = self._head
        return self

    def __next__(self):
        if not self._current:
            raise StopIteration
        else:
            item = self._current.data
            self._current = self._current.link
            return item

    def __getitem__(self, index):
        return self.__get_node_at(index).data

    def __str__(self) -> str:
        string = ""
        current = self.head
        while current is not None:
            string += str(current.val)
            if current is not self.tail:
                string += ", "
            current = current.next
        return string
