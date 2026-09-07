class Solution:
    def isValid(self, s: str) -> bool:
        i=0
        a=[]
        for i in range(len(s)):
           if(s[i]=='{' or s[i]=="[" or s[i]=='('):
            a.append(s[i])
           else:
            if len(a)==0:
                return False
            if(s[i]=="}" and a[-1]!="{"):
                return False
            if(s[i]=="]" and a[-1]!="["):
                return False
            if(s[i]==")" and a[-1]!="("):
                return False
            a.pop()

        return len(a)==0
