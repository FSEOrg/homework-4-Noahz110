# https://leetcode.com/problems/intervals-between-identical-elements/submissions/

class Solution:
    """
    left_sum[i]: sum of intervals of arr[:i]
    right_sum[i]: sum of intervals of arr[i:]
    => intervals[i] = left_sum[i] + right_sum[i]
    try left_sum of all element has value = 3
 arr     2 1 3 1 2 3 3
 idx     0 1 2 3 4 5 6
             *     * *

    left_sum[2] = 0     
    left_sum[5] = 5-2 = 0 + (5 - 2) * 1 = left_sum[2] + (5-2)*1                                     
    left_sum[6] = (6-2) + (6-5) = (6-5) + (5-2) + (6-5) = (5-2) + (6-5) * 2 = left_sum[5] + (6-5)*2

    => left_sum[i] = left_sum[prev_i] + |i - prev_i| * (count of elements = value)

    counter: a dict contain (key, value) = value of element, (last index of element = value, total count of element = value)
    for arr from left to right => left_sum

    similarly, calculate right_sum[i]

    Time: O(n)
    Space: O(n)
    """
    def get_prefix_sum(self, arr, iters):
        counter = collections.defaultdict()
        prefix_sum = [0] * len(arr)
        for i in iters:
            if arr[i] not in counter:
                counter[arr[i]] = (i, 1)
                prefix_sum[i] = 0
                continue
            prev_i, prev_count = counter[arr[i]]
            prefix_sum[i] = prefix_sum[prev_i] + abs(i - prev_i) * prev_count
            counter[arr[i]] = (i, prev_count + 1)
        return prefix_sum

    def getDistances(self, arr: List[int]) -> List[int]:
        left_sum = self.get_prefix_sum(arr, range(len(arr)))
        right_sum = self.get_prefix_sum(arr, range(len(arr) - 1, -1, -1))

        res = []
        for i in range(len(arr)):
            res.append(left_sum[i] + right_sum[i])
        return res
            

