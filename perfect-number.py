class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return True if sum([_num + (num / _num) for _num in range(1, int(sqrt(num)+1)) if num % _num == 0]) - num == num and num > 1 else False
        
