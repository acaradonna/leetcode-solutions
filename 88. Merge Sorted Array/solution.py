class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize pointers
        p1 = m - 1  # Pointer for nums1 (starting from last valid element)
        p2 = n - 1  # Pointer for nums2 (starting from last element)
        p = m + n - 1  # Pointer for the merged array (starting from last position)
        
        # While there are elements to compare
        while p2 >= 0:
            # If p1 is still valid and nums1[p1] is greater than nums2[p2]
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

# Example usage:
if __name__ == "__main__":
    # Test case 1
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(f"Test case 1 result: {nums1}")  # Expected: [1,2,2,3,5,6]
    
    # Test case 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    Solution().merge(nums1, m, nums2, n)
    print(f"Test case 2 result: {nums1}")  # Expected: [1]
    
    # Test case 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    Solution().merge(nums1, m, nums2, n)
    print(f"Test case 3 result: {nums1}")  # Expected: [1] 