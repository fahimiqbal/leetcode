class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mergedList = list1 + list2
        itemList = {}
        matchList = []

        for i, v in enumerate(mergedList):
            if v in itemList:
                itemList[v] += i
                matchList.append(v)
            else:
                itemList[v] = i

        finalList = []
        min = 0
        for item in matchList:
            if min == 0:
                min = itemList[item]
            if itemList[item] < min:
                finalList = [item]
            elif itemList[item] == min:
                finalList.append(item)

        return finalList