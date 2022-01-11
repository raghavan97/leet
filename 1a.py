class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cntr = 0
        nums1 = []
        for i in nums:
            nums1.append((i,cntr))
            cntr += 1

        nums1.sort()

        left = 0
        n = len(nums) -1
        right = n

        while left < right:
            a = nums1[left][0]
            b = nums1[right][0]
            sum = a + b

            if sum < target:
                left +=1
                continue

            if sum > target:
                right -= 1
                continue

            if sum == target:
                return nums1[left][1],nums1[right][1]

