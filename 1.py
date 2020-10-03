# leet code - problem - 1
# Traverse the array of integers num and make a presence dict indicating 
# the presence of the number, if the counterpart is already present, then
# we return the two indexes


class Solution(object):

    def twoSum(self, nums, target):
        presence = {}

        index = 0
        x = 0
        y = 0

        for i in nums:
            counterpart = target - i
            if counterpart in presence:
                x = presence[counterpart]
                y = index
                return x, y
            if i not in presence:
                presence[i] = index
            index += 1

        return x, y

if __name__ == "__main__":
    m=Solution()
    res = m.twoSum([3,2,4],6)
    print(res)
    res = m.twoSum([3,3],6)
    print(res)
