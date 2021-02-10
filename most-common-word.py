from collections import Counter
import re
from typing import List
#re.sub(r'[^\w]', ' ', paragraph): 단어문자가 아닌 모든 문자를 공백으로 치환
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        low_word = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        return Counter(low_word).most_common(1)[0][0]