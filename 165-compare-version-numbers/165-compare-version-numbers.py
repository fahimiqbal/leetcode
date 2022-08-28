class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        if version1 == version2:
            return 0
        v1List = [int(k) for k in version1.split('.')]
        v2List = [int(k) for k in version2.split('.')]

        maxLen = max(len(v1List), len(v2List))

        for i in range(maxLen):
            if i < len(v1List):
                v1 = v1List[i]
            else:
                v1 = 0

            if i < len(v2List):
                v2 = v2List[i]
            else:
                v2 = 0

            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1

        return 0