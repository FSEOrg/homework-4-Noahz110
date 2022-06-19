# https://leetcode.com/problems/valid-anagram/

class Solution:
    """
    get_hash return a tuple of frequency of a char in string
    if get_hash(s) == get_hash(t) => true
    
    Time O(len(s))
    Space O(len(s))
    """
    def get_hash(self, s):
        count = [0] * 26
        for char in s:
            count[ord(char) - ord("a")] += 1
        return tuple(count)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        if self.get_hash(s) == self.get_hash(t):
            return True
        return False
