
# h = [1,8,6,2,5,4,8,3,7]
#     [0,1,2,3,4,5,6,7,8]
# 
# Brute force:
#     1,8 calculate its container area
#     1,6 calculate its container area
#     1,2 calculate its container area
#     and so on
#     repeat for 8,6,2 etc until 3

# Optimized
# have a left pointer at the start and right pointer at the end
# left=0 , lval = 1
# right=8, rval = 7
# The max_area beween these two cannot exceed 1*(8-0) = 8, even if there are higher numbers in between
# This exhausts 1,*
# move the left pointer by one step , since lval < rval
# h = [*,8,6,2,5,4,8,3,7]
#     [0,1,2,3,4,5,6,7,8]
# 
# left=1, lval = 8
# right=8, rval = 7
# The max_area beween these two cannot exceed 7*(8-1) = 49, even if there are higher numbers in between
# This exhausts *,7
# move the right pointer by one step , since rval < lval
# h = [*,8,6,2,5,4,8,3,*]
#     [0,1,2,3,4,5,6,7,8]
# 
# left=1, lval = 8
# right=7, rval = 3
# The max_area beween these two cannot exceed 3*(7-1) = 18, even if there are higher numbers in between
# This exhausts *,3
# move the right pointer by one step , since rval < lval
# h = [*,8,6,2,5,4,8,*,*]
# 
# left=1, lval = 8
# right=6, rval = 8
# The max_area beween these two cannot exceed 8*(6-1) = 40, even if there are higher numbers in between
# This exhausts 8,*
# move the left pointer by one step , since lval == rval
# h = [*,*,6,2,5,4,8,*,*]
#     [0,1,2,3,4,5,6,7,8]
# 
# left=2, lval = 6
# right=6, rval = 8
# The max_area beween these two cannot exceed 6*(6-2) = 24, even if there are higher numbers in between
# This exhausts 6,*
# move the left pointer by one step , since lval < rval
# h = [*,*,*,2,5,4,8,*,*]
#     [0,1,2,3,4,5,6,7,8]
# 
# left=3, lval = 2
# right=6, rval = 8
# The max_area beween these two cannot exceed 2*(6-3) = 6, even if there are higher numbers in between
# This exhausts 2,*
# move the left pointer by one step , since lval < rval
# h = [*,*,*,*,5,4,8,*,*]
#     [0,1,2,3,4,5,6,7,8]
# 
# left=4, lval = 5
# right=6, rval = 8
# The max_area beween these two cannot exceed 5*(6-4) = 10, even if there are higher numbers in between
# This exhausts 5,*
# move the left pointer by one step , since lval < rval
# h = [*,*,*,*,*,4,8,*,*]
#     [0,1,2,3,4,5,6,7,8]
# 
# left=5, lval = 4
# right=6, rval = 8
# The max_area beween these two cannot exceed 4*(6-5) = 4, even if there are higher numbers in between
# This exhausts 4,*
# move the left pointer by one step , since lval < rval
# now left will be 6 and right is also 6, we break out
# h = [*,*,*,*,*,*,8,*,*]
#     [0,1,2,3,4,5,6,7,8]
# 

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            lval = height[left]
            rval = height[right]
            w = right - left

            if lval <= rval:
                area = lval*w
                if area > max_area:
                    max_area = area
                # everything that starts with left
                # is exhausted
                left += 1
                continue

            if lval > rval:
                area = rval * w
                if area > max_area:
                    max_area = area
                # everything that ends with right
                # is exhausted

                right -= 1
                continue

        return max_area

if __name__ == "__main__":
    s = Solution()
    h = [1,8,6,2,5,4,8,3,7]
    ret=s.maxArea(h)
    print(ret)
