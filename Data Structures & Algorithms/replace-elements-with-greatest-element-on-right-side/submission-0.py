class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            start = i + 1       
            if len(arr[start:]) > 0:
                arr[i] = max(arr[start:])
        arr[-1] = -1
        return arr