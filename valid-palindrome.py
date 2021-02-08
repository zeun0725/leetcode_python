# https://leetcode.com/problems/valid-palindrome/submissions/
import re

class Solution:
    def rm_not_eng_num(self, s: str) -> str:
        low_s = s.lower()
        return re.sub('[^0-9a-z]', '', low_s)

    def isPalindrome(self, s: str) -> bool:
        text = self.rm_not_eng_num(s)
        if text[::-1].__eq__(text):
            return True
        return False
