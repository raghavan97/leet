class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        n = len(numbers) - 1
        right = n

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum > target:
                right -=1
                continue

            if sum < target:
                left += 1
                continue

            if sum == target:
                return (left+1, right+1)

s = Solution()
numbers=[2,7,11,15]
target = 9
m=s.twoSum(numbers, target)
print(m)
