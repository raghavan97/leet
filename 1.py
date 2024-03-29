# leet code - problem - 1
# Traverse the array of integers num and make a presence dict indicating 
# the presence of the number, if the counterpart is already present, then
# we return the two indexes


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        presence = {}

        for index, val in enumerate(nums):
            counterpart = target - val
            if counterpart in presence:
                x = presence[counterpart]
                y = index
                return x, y
            presence[val] = index

if __name__ == "__main__":
    m=Solution()
    res = m.twoSum([3,2,4],6)
    print(res)
    res = m.twoSum([3,3],6)
    print(res)
