class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=s.replace(" ","")
        s = ''.join(c for c in s if c.isalnum())
        print(s)
        i=0
        j=len(s)-1
        for i in range(len(s)):
            if s[i]!=s[j]:
                return False
                break
            j=j-1
        return True