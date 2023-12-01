class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m-1, n-1, m+n-1
        
        while j >= 0:
            if i < 0 or nums2[j] > nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        
        # This step is not necessary as Python's list assignment will overwrite 
        # the elements, and since we are merging into nums1, any remaining elements 
        # in nums1 are already in their correct position.
