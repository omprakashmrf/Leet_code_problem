class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        resulted = []
        if len(nums1) >0:
            resulted.extend(nums1)

        if len(nums2)>0:
            resulted.extend(nums2)
        resulted.sort()    
        while resulted:
            if len(resulted) %2==1:
                # mid=((len(resulted))//2)
                median=float(resulted[((len(resulted))//2)])
                return median
            else:
                mid = len(resulted)//2
                median = (float(resulted[mid-1])+float(resulted[mid]))/2.0
                return median




        