'''
LeetCode 66. Plus One
Language : Python
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus_num =  int(''.join(map(str, digits))) + 1
        return [int(x) for x in str(plus_num)]