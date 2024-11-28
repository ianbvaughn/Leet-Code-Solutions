import math
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr=nums1+nums2
        for i in range(len(arr)-1):
            for j in range(len(arr)-1):
                if arr[j]<=arr[j+1]:
                    continue
                else:
                    curr=arr[j]
                    arr[j]=arr[j+1]
                    arr[j+1]=curr
        if len(arr)%2 == 1:
            return arr[int(math.floor(len(arr)/2))]
        else:
            return float((arr[int(len(arr)/2)-1]+arr[int(len(arr)/2)]))/2