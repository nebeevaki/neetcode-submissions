class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m -= 1
        n -= 1
        for left in range(len(nums1) -1, -1, -1):
            if n < 0 or (nums1[m] >= nums2[n] and m >= 0):
                nums1[left] = nums1[m]
                m -= 1
            else:
                nums1[left] = nums2[n]
                n -=1