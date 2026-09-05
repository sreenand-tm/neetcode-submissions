class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            arr = [0] * 128   
            for i in range(0, len(s)):
                arr[ord(s[i])] += 1
            for i in range(0, len(t)):
                arr[ord(t[i])] -= 1
                if arr[ord(t[i])] < 0:
                    return False

            return True