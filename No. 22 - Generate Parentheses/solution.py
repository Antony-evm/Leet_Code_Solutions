# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

#  1 <= n <= 8

 class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        import itertools
        def isvalid(l):
            l = l[::-1]
            while l!='':
                if l.find(')(')>=0:
                    l=l.replace(')(','')
                else:
                    return False
            return True
        s = [None]*n*2
        s[0],s[-1] = '(',')'
        res = []
        for i in itertools.combinations(range(1,len(s)-1),n-1):
            for idx in range(1,len(s)-1):
                if idx in i:
                    s[idx]='('
                else:
                    s[idx]=')'
            res.append(''.join(s))
            s[1:-1] = [None]*(n*2-2)
        return [i for i in res if isvalid(i)]
      


            