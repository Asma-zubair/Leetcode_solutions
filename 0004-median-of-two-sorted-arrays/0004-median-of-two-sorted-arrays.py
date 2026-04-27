class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1

        m=len(nums1)
        n=len(nums2)
        low=0 
        high=m

        while low <=high:
            left_size=(m+n+1)//2
            cut1=(low+high)//2
            cut2=left_size - cut1

            if cut1 == 0 :
                l1=float('-inf')
            else:
                l1=nums1[cut1-1]

            if cut1 == m:
                r1=float('inf')
            else:
                r1=nums1[cut1]

            if cut2 == 0 :
                l2=float('-inf')
            else:
                l2=nums2[cut2-1]
            
            if cut2 == n:
                r2 = float('inf')
            else:
                r2 = nums2[cut2]

            if l1 <= r2 and l2 <= r1:
                if (m+n)%2==0:
                    return(max(l1,l2)+ min(r1,r2))/2
                else:
                    return(max(l1,l2))

            elif l1 > r2:
                high=cut1-1
            else:
                low=cut1+1


            