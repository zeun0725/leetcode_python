# https://leetcode.com/problems/reverse-string/submissions/
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]
        """
        Do not return anything, modify s in-place instead.
        """
