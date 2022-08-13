class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        done = 0
        for n in range(200):
            pr = ''
            for i in range(len(strs)):
                if n >= len(strs[i]):
                    done = 1
                    break
                if i == 0:
                    pr = strs[i][n]
                if strs[i][n] != pr:
                    done = 1
                    break
            if done == 1:
                break
            prefix += pr
        return prefix