
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        imax = 0
        omax = 0
        i = 0
        j = 0
        a = {}

        while j < len(s):

            if s[j] not in a:
                a[s[j]] = j
                j = j + 1
                imax = j - i

            else:
                i = max(i, a[s[j]] + 1)
                a[s[j]] = j
                j = j + 1
                imax = j - i

            if imax > omax:
                omax = imax

        return omax

