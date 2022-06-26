class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=''
        # outer,inner=0,0
        # for i in s:
        #     if i=='(':
        #         if outer==0:
        #             outer+=1
        #         else:
        #             inner+=1
        #             ans+=i
        #     elif i==')':
        #         if inner>0:
        #             ans+=i
        #             inner-=1
        #         else:
        #             outer-=1A
        # return ans
        
        stack=[]
        for i in s:
            if i=='(' and len(stack)==0:
                stack.append(i)
                continue
            elif i==')' and stack[-1]=='(':
                stack.pop()
                if len(stack)!=0:
                    ans+=i
                    continue
                else:
                    continue
            stack.append(i)
            ans+=i
        return ans