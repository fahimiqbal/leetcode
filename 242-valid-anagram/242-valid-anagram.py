class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = len(s)

        list1 = {}
        list2 = {}

        for l in range(count):
            if s[l] not in list1.keys():
                list1[s[l]] = 1
            else:
                list1[s[l]] += 1

            if t[l] not in list2.keys():
                list2[t[l]] = 1
            else:
                list2[t[l]] += 1

        if list1 == list2:
            return True

        return False