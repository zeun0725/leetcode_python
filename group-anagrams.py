from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_count = defaultdict(list)
        for string in strs:
            str_count[str(sorted(string))].append(string)
        return str_count.values()
