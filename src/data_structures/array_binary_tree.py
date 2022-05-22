"""Array representation of a binary tree"""
from collections import deque


class ArrayBinaryTree:
    """
    Reparesent a binary tree in array format.

    The array need to be with length 2^H - 1, where H is the height of the tree

    For each node at idx:
        left child: (idx * 2) + 1: odd numbers [1, 3, 5 ...]
            parent: (idx - 1) // 2
        right child: (idx * 2) + 2: even numbers [2, 4, 6 ...]
            parent: (idx - 2) // 2
    """

    def __init__(self, height: int = 1):
        self.tree = [None] * (2**height - 1)

    @classmethod
    def _get_root_idx(cls):
        return 0

    @classmethod
    def _get_left_child_idx(cls, idx):
        return (idx * 2) + 1

    @classmethod
    def _get_right_child_idx(cls, idx):
        return (idx * 2) + 2

    @classmethod
    def _get_parent_idx(cls, idx):
        return (idx - 2) // 2 if idx % 2 == 2 else (idx - 1) // 2

    def _get_idx(self, idx):
        if idx >= len(self.tree) or not self.tree[idx]:
            raise IndexError("Node not found.")
        return self.tree[idx]

    def set_root(self, value):
        """Set a value to the root node

        Args:
            value (Any): the value to be set

        Returns:
            int: the array index of the root node
        """
        idx = self._get_root_idx()
        self.tree[idx] = value
        return idx

    def set_left(self, idx, value):
        """Set a value to the left children of a given index

        Args:
            idx (int): the idx of the selected node
            value (int): the value to be set to the left children of the selected node

        Returns:
            int: the array index of the added children
        """
        self._get_idx(idx)  # make sure it is a valid move
        target_idx = self._get_left_child_idx(idx)
        self.tree[target_idx] = value
        return target_idx

    def set_right(self, idx, value):
        """Set a value to the right children of a given index

        Args:
            idx (int): the idx of the selected node
            value (int): the value to be set to the right children of the selected node

        Returns:
            int: the array index of the added children
        """
        self._get_idx(idx)  # make sure it is a valid move
        target_idx = self._get_right_child_idx(idx)
        self.tree[target_idx] = value
        return target_idx

    def print_tree(self):
        """Print out the tree level by level

        Returns:
            list[list[int]]: 2D arrays to represent the tree level by level
        """
        # Level-wise
        q = deque()
        q.append((self._get_root_idx(), 0))

        printing_level = 0
        levels = []
        level_values = []

        while q:
            curr_idx, curr_level = q.popleft()
            if curr_level == printing_level:
                level_values.append(str(self.tree[curr_idx]))
            else:
                print(f"Level-{printing_level}: {level_values}")
                printing_level = curr_level
                levels.append(level_values)
                level_values = [str(self.tree[curr_idx])]

            left_idx = self._get_left_child_idx(curr_idx)
            right_idx = self._get_right_child_idx(curr_idx)

            if left_idx < len(self.tree):
                q.append((left_idx, curr_level + 1))
            if right_idx < len(self.tree):
                q.append((right_idx, curr_level + 1))

        print(f"Level-{printing_level}: {level_values}")
        levels.append(level_values)
        return levels
