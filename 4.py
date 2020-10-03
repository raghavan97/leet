# leet code - problem - 4

# merge the 2 sorted lists and give out the median
# The median is the value of middle element of the array
# in case the length is even , then it is the average of 2 middle elements
# [1, 5, 6, 7, 9 ] , median=6
# [1, 5, 6, 7, 9, 15] , median = (6 + 7)/2 = 6.5

class Solution(object):

    def mergeLists(self, nums1, nums2):

        nums3 = []

        p1 = 0
        p2 = 0
        p3 = 0

        n1 = len(nums1)
        n2 = len(nums2)
        n3 = n1 + n2

        nums3 = [None]*n3

        while p3 < n3:
            if p1 >= n1:
                nums3[p3] = nums2[p2]
                p3 += 1
                p2 += 1
                continue

            if p2 >= n2:
                nums3[p3] = nums1[p1]
                p3 += 1
                p1 += 1
                continue

            if nums1[p1] <= nums2[p2]:
                nums3[p3] = nums1[p1]
                p1 += 1
            else:
                nums3[p3] = nums2[p2]
                p2 += 1

            p3 += 1
            # print("p1={} p2={} p3={}".format(p1,p2,p3))

        self.nums3 = nums3
        self.n3 = n3

    def getMedian(self):
        n = self.n3
        nums3 = self.nums3
        # [1, 5, 7, 8, 9] len=5
        # median = (5+1)/2 = 3rd value, since index starts at 0, it is index=2

        rem = n%2
        if rem == 0:
            # len = 6 , means nums[2], nums[3] 
            index1 = n/2 - 1
            index2 = index1 + 1
            sum = nums3[index1] + nums3[index2]
            return float(sum)/2
        else:
            index = ((n+1)/2) - 1
            return nums3[index]



    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        self.mergeLists(nums1, nums2)
        # print(self.nums3)
        return self.getMedian()




if __name__ == "__main__":
    s = Solution()
    # res = s.findMedianSortedArrays([1,2,3,3,4,7,9,23], [2,4,6,8,9,9])
    # print(res)
    res = s.findMedianSortedArrays([1,2], [3,4])
    print(res)

