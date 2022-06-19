# https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        prefix: sum all elements from index 0 -> i
        hash table: key, value = prefix[i], frequency of prefix
        foreach num in nums: if exist j where prefix[num] - prefix[j] = k => count += frequency
        
        [0,1,2,3], k =3
prefix 0 0 1 3 6
freq   1 2 1 1 1
count  0 0 0 2 3
        
        Time: O(n)
        Space: O(n)
        """
        res = 0
        total = 0
        counter = {total: 1}
        for num in nums:
            total += num
            if total - k in counter:
                res += counter[total - k]
            counter[total] = counter.get(total, 0) + 1
        return res
