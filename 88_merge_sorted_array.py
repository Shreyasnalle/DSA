class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1_end_pointer = m - 1 
        nums2_end_pointer = n - 1
        final_pointer = m + n - 1
        while nums1_end_pointer >= 0 and nums2_end_pointer >= 0 :
            if nums2[nums2_end_pointer] > nums1[nums1_end_pointer] :
                nums1[final_pointer] = nums2[nums2_end_pointer]
                nums2_end_pointer -= 1
            else :
                nums1[final_pointer] = nums1[nums1_end_pointer]
                nums1_end_pointer -= 1
            final_pointer -= 1
        while nums2_end_pointer >= 0 :
            nums1[final_pointer] = nums2[nums2_end_pointer]
            nums2_end_pointer -= 1
            final_pointer -= 1