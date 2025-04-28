class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if 0 in nums1: nums1 = list(filter(lambda num: num != 0,nums1))
        if 0 in nums2: nums2 = list(filter(lambda num: num != 0,nums2))
        nums=[]
        if m == 0:
            nums = nums2
        elif n == 0:
            nums = nums1
        else:
            for i in range (min(m,n)):
                if nums1[0] < nums2[0]:
                    nums.append(nums1[0])
                    nums1.pop(0)
                else:
                    nums.append(nums2[0])
                    nums2.pop(0)
            nums+=nums1+nums2
            return nums

a = Solution()
b=a.merge([1,2,3,0,0,0],3,[2,5,6],3)
print(b)