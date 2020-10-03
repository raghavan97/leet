# leet code - problem - 3

# abcabcbb
# all possible substrings

# len = 8
# a, ab, abc, abca, abcab, abcabc, abcabcb, abcabcbb (8)
# b, bc, bca, bcab, bcabc, bcabcb, bcabcbb (7)
# c, ca, cab, cabc, cabcb, cabcbb (6)
# a, ab, abc, abcb, abcbb (5)
# b, bc, bcb, bcbb (4)
# c, cb, cbb (3)
# b, bb (2)
# b (1)
# This is a AP 1+2+3+4+....8 = (8)(8+1)/2 = 36
# The total substrings for a string of size 'n' is
# (n)(n+1)/2 from the above

# We dont have to generate all possible substrings, we can stop when
# we encounter the first repeat of char, for example, in the first
# row we only need to generate a, ab, abc, the abca is useless

# Sliding Window
# with 2 pointers , left and right , we look at a substring and see if it has
# repeats
# when there is a repeat, then we move the left by one
# when there is no repeat , we move the right
# we also check a substring only if it is longer than what already have

class Solution(object):

    def repeat(self, s):
        l1 = len(set(s))
        l2 = len(s)
        if l1 < l2:
            return True
        return False

    # sliding window
    def slidingWindowLengthOfLongestSubstring(self, s):

        # no brainers
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        left = 0
        right = 1
        longest = 1
        n = len(s)
        while right <=  n:
            # s = "raghavan" , then s[0:1] = 'r' , s[0:2] = 'ra'
            substr = s[left:right]
            substr_len = right - left

            if substr_len <= longest:
                right += 1
                continue

            if self.repeat(substr):
                # there is a repeat, we move the left of the window
                left += 1
                continue

            # no repeat , this is the longest we have seen
            longest = right - left
            right += 1

        return longest

    def bruteForceLengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        i = 0
        longest = 0
        while i < l:
            j = i + 1
            # s="abcde" len=5, s[0:1]='a', s[0:4]='abcd', s[0:5]='abcde'
            while j <= l:
                substr_len = j - i
                substr = s[i:j]
                # print(substr)
                if not self.repeat(substr):
                    if substr_len > longest:
                        longest = substr_len
                j += 1
            i += 1
            # print("===========")

        # print("longest = {}".format(longest))
        return longest

    def bruteForceOptLengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        i = 0
        longest = 0
        while i < l:
            j = i + 1
            # s="abcde" len=5, s[0:1]='a', s[0:4]='abcd', s[0:5]='abcde'
            while j <= l:
                substr_len = j - i
                # print(substr)

                # dont bother - not longer than what we already know
                if substr_len <= longest:
                    j += 1
                    continue

                substr = s[i:j]

                # for s = "abcabcbb"
                # a, ab, abc, abca, abcab, abcabc, abcabcb, abcabcbb (8)
                # once you find abca, there is no point checking abcab
                if self.repeat(substr):
                    break

                longest = substr_len
                j += 1

            i += 1
            # print("===========")

        # print("longest = {}".format(longest))
        return longest

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # return self.slidingWindowLengthOfLongestSubstring(s)
        # return self.bruteForceLengthOfLongestSubstring(s)
        return self.bruteForceOptLengthOfLongestSubstring(s)




if __name__ == "__main__":
    m = Solution()
    result = m.lengthOfLongestSubstring("abcabcbb")
    print(result)
    result = m.lengthOfLongestSubstring("")
    print(result)
    result = m.lengthOfLongestSubstring("au")
    print(result)
    result = m.lengthOfLongestSubstring("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABC")

    print(result)
