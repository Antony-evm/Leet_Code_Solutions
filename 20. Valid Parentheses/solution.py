Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        def count_occurences(openList:List,closeList:List,s:str)->bool:
            return all([s.count(openChar)==s.count(closeChar) for openChar,closeChar in zip(openList,closeList)])
        marker = ''
   
        if len(s)%2!=0 | count_occurences('({[',')}]',s) == False:
            return False
        else:
            s=s[::-1]
            while s!='':
                a = s.find(')(')
                if a>=0:
                    s = s[:a]+s[a+2:]
                    marker = 'a'
                b=s.find('][')
                if b>=0:
                    s = s[:b]+s[b+2:]
                    marker = 'b'
                c=s.find('}{')
                if c>=0:
                    s = s[:c]+s[c+2:]
                    marker = 'c'
                if marker == '':
                    return False
                else:
                    marker = ''

            return True

        