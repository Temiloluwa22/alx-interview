#!/usr/bin/python3
"""
Module for lockboxes.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    keys = set([0])  # Set to store box numbers that can be opened
    stack = [0]  # Stack to keep track of boxes to explore

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key < len(boxes) and key not in keys:
                keys.add(key)
                stack.append(key)

    return len(keys) == len(boxes)

# Example usage
if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # False
