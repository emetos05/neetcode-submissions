class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        m = len(nums)

        while k < m:
            if nums[k] == val:
                m -= 1
                nums[k] = nums[m]
            else:
                k += 1
        return k