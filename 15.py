class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        n = len(nums) - 1
        triplets = []

        print(nums)

        for i, val in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            a = val
            left = i + 1
            right = n

            while left < right:
                b = nums[left]
                c = nums[right]
                sum = a + b + c

                print(f"trying {a}:{i},{b}:{left},{c}:{right}")

                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -=1
                else:
                    triplets.append((a,b,c))
                    left += 1

                    while left < right:
                        if nums[left] == nums[left-1]:
                            left += 1
                        

                last_left = b


        return triplets

if __name__ == "__main__":
    s = Solution()
    # res = s.threeSum([2,-2,0])
    # print(res)
    # res = s.threeSum([0,0,0])
    # print(res)
    inp = [-2,0,1,1,2]
    inp = [-1,0,1,2,-1,-4]
    inp = [0,0,0, 0]
    # inp = [-1,0,1,0]
    # inp = [1,-1,-1,0]
    res = s.threeSum(inp)
    print(res)

