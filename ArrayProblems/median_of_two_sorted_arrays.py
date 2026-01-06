'''Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.'''
def MedianOfTwoSortedArrays(arr1, arr2):
    merged_array = sorted(arr1 + arr2)
    n = len(merged_array)
    if n % 2 == 1:
        return merged_array[n // 2]
    else:
        mid = merged_array[n // 2 - 1 : n // 2 + 1]
        return sum(mid) / 2

def main():
    arr1 = [1,2]
    arr2 = [3,4]
    result = MedianOfTwoSortedArrays(arr1, arr2)
    print("Median of two sorted arrays is:", result)

    arr1 = [2,2,4,4]
    arr2 = [2,2,2,4,4]
    result = MedianOfTwoSortedArrays(arr1, arr2)
    print("Median of two sorted arrays is:", result)

if __name__ == "__main__":
    main()