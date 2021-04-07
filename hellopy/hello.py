'''
Created on 8 Nov 2019

@author: odys-z@github.com
'''

def main():
    sol = Solution()
    sol.generateParenthesis(3)


class Solution(object):
    ''' 22. Generate Parentheses
        https://leetcode-cn.com/problems/generate-parentheses/
    '''
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        tree = list(self.dfs(n - 1))
        print(tree)
        return tree
    
    def dfs(self, sublvl):
        '''dfs of subtree
            returns
            -------
            str of "()" pairs
        '''
        if sublvl > 0:
            tree = set()
            subtree = self.dfs(sublvl - 1)
            for subtr in subtree:
                tree.update([
                    "(" + subtr + ")",
                    "()" + subtr,
                    subtr + "()"])
            return tree
        else:
            return ["()"]
        
main()