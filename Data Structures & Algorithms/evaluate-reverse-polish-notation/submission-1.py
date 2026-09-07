class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op=[]
        j=0
        for i in tokens:
            j=j+1
            if i.lstrip('-').isnumeric():
                op.append(int(i))
            else:
                a=int(op.pop())
                b=int(op.pop())
                if(i=='+'):
                    op.append(a+b)        
                if(i=='-'):
                    op.append(b-a)
                if(i=='*'):
                    op.append(a*b)
                if(i=='/'):
                    op.append(int(b/a))
            if j==len(tokens):
                return int(op.pop())    