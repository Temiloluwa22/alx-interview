#!/usr/bin/python3
""" Module for pascal_triangle function """


def pascal_triangle(n):
    """Creates a pascal triangle"""
    if n <= 0:
        return []
    triangle = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, i + 1):
            if j == 1 or j == i or i <= 2:
                element = 1
            else:
                element = triangle[i - 2][j - 1] + triangle[i - 2][j - 2]
            row.append(element)
        triangle.append(row)
    return triangle
