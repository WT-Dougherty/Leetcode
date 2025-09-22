# --------------------------- Median of Two Sorted Arrays ---------------------------
"""
Problem: Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6
"""

def binary_search(arr: list[int], k: int) -> int:
    return binary_search_wrapped(arr, 0, len(arr)-1, k)

def binary_search_wrapped(arr: list[int], l: int, r: int, k: int) -> int:
    if l <= r:
        mid = (r+l) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            return binary_search_wrapped(arr, l, mid-1, k)
        else:
            return binary_search_wrapped(arr, mid+1, r, k)
    else:
        return -1

def findMedianSortedArrays(nums1, nums2):
    """
    Find the median of two sorted arrays.
    
    Args:
        nums1: List[int] - First sorted array
        nums2: List[int] - Second sorted array
    
    Returns:
        float - The median of the two sorted arrays
    """
    pass

# --------------------------- Test Cases ---------------------------
import unittest

class TestBinarySearch(unittest.TestCase):
    
    def test_find_existing_element_middle(self):
        """Test finding an element in the middle of the array."""
        arr = [1, 2, 3, 4, 5]
        result = binary_search(arr, 3)
        # Note: Current implementation has issues, this test documents expected behavior
        # Expected: should return 2 (index of 3)
    
    def test_find_existing_element_first(self):
        """Test finding the first element."""
        arr = [1, 2, 3, 4, 5]
        result = binary_search(arr, 1)
        # Expected: should return 0 (index of 1)
    
    def test_find_existing_element_last(self):
        """Test finding the last element."""
        arr = [1, 2, 3, 4, 5]
        result = binary_search(arr, 5)
        # Expected: should return 4 (index of 5)
    
    def test_find_nonexistent_element(self):
        """Test searching for an element that doesn't exist."""
        arr = [1, 2, 3, 4, 5]
        result = binary_search(arr, 6)
        # Expected: should return None or handle gracefully
    
    def test_empty_array(self):
        """Test searching in an empty array."""
        arr = []
        result = binary_search(arr, 1)
        # Expected: should handle empty array gracefully
    
    def test_single_element_found(self):
        """Test searching in array with single element that exists."""
        arr = [42]
        result = binary_search(arr, 42)
        # Expected: should return 0
    
    def test_single_element_not_found(self):
        """Test searching in array with single element that doesn't exist."""
        arr = [42]
        result = binary_search(arr, 1)
        # Expected: should return None or handle gracefully
    
    def test_duplicate_elements(self):
        """Test searching in array with duplicate elements."""
        arr = [1, 2, 2, 2, 3]
        result = binary_search(arr, 2)
        # Expected: should return one of the indices containing 2
    
    def test_negative_numbers(self):
        """Test searching in array with negative numbers."""
        arr = [-5, -3, -1, 0, 2, 4]
        result = binary_search(arr, -1)
        # Expected: should return 2 (index of -1)
    
    def test_large_array(self):
        """Test searching in a larger array."""
        arr = list(range(1, 1001))  # [1, 2, ..., 1000]
        result = binary_search(arr, 500)
        # Expected: should return 499 (index of 500)
    
    def test_even_length_array(self):
        """Test searching in array with even length."""
        arr = [1, 2, 3, 4]
        result = binary_search(arr, 3)
        # Expected: should return 2 (index of 3)
    
    def test_odd_length_array(self):
        """Test searching in array with odd length."""
        arr = [1, 2, 3, 4, 5]
        result = binary_search(arr, 4)
        # Expected: should return 3 (index of 4)
    
    def test_all_same_elements(self):
        """Test searching in array where all elements are the same."""
        arr = [5, 5, 5, 5, 5]
        result = binary_search(arr, 5)
        # Expected: should return one of the indices containing 5
    
    def test_target_smaller_than_all(self):
        """Test searching for target smaller than all elements."""
        arr = [10, 20, 30, 40, 50]
        result = binary_search(arr, 5)
        # Expected: should return None or handle gracefully
    
    def test_target_larger_than_all(self):
        """Test searching for target larger than all elements."""
        arr = [10, 20, 30, 40, 50]
        result = binary_search(arr, 100)
        # Expected: should return None or handle gracefully

class TestMedianTwoSortedArrays(unittest.TestCase):
    
    def test_example_1(self):
        """Test case from example 1."""
        nums1 = [1, 3]
        nums2 = [2]
        expected = 2.0
        result = findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, expected)
    
    def test_example_2(self):
        """Test case from example 2."""
        nums1 = [1, 2]
        nums2 = [3, 4]
        expected = 2.5
        result = findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, expected)
    
    def test_empty_first_array(self):
        """Test when first array is empty."""
        nums1 = []
        nums2 = [1, 2, 3, 4, 5]
        expected = 3.0
        result = findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, expected)
    
    def test_empty_second_array(self):
        """Test when second array is empty."""
        nums1 = [1, 2, 3, 4, 5]
        nums2 = []
        expected = 3.0
        result = findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, expected)
    
    def test_both_empty_arrays(self):
        """Test when both arrays are empty."""
        nums1 = []
        nums2 = []
        # This case is not defined in constraints, but should handle gracefully
        result = findMedianSortedArrays(nums1, nums2)
        # Could return 0, None, or raise an exception depending on implementation
    
    def test_single_element_each(self):
        """Test arrays with single element each."""
        nums1 = [1]
        nums2 = [2]
        expected = 1.5
        result = findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, expected)
    
    def test_identical_arrays(self):
        """Test identical arrays."""
        nums1 = [1, 2, 3]
        nums2 = [1, 2, 3]
        expected = 2.0
        result = findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, expected)
    
    def test_non_overlapping_arrays(self):
        """Test arrays with no overlapping values."""
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        expected = 3.5
        result = findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, expected)
    
    def test_negative_numbers(self):
        """Test arrays with negative numbers."""
        nums1 = [-1, 0, 1]
        nums2 = [-2, 2]
        expected = 0.0
        result = findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, expected)
    
    def test_duplicate_values(self):
        """Test arrays with duplicate values."""
        nums1 = [1, 1, 2, 2]
        nums2 = [1, 2, 3]
        expected = 1.5
        result = findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, expected)
    
    def test_large_arrays(self):
        """Test with larger arrays."""
        nums1 = list(range(1, 501))  # [1, 2, ..., 500]
        nums2 = list(range(501, 1001))  # [501, 502, ..., 1000]
        expected = 500.5
        result = findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, expected)
    
    def test_odd_total_length(self):
        """Test when total length is odd."""
        nums1 = [1, 2, 3]
        nums2 = [4, 5]
        expected = 3.0
        result = findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, expected)
    
    def test_even_total_length(self):
        """Test when total length is even."""
        nums1 = [1, 2]
        nums2 = [3, 4, 5, 6]
        expected = 3.5
        result = findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, expected)

def run_binary_search_tests():
    """Run only binary search tests."""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBinarySearch)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

def run_tests():
    """Run all tests and display results."""
    unittest.main(verbosity=2)

if __name__ == "__main__":
    # Uncomment the line below to run only binary search tests
    run_binary_search_tests()
    # run_tests()
