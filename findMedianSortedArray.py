class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if not nums1:
            if len(nums2) % 2 == 0:
                return (nums2[len(nums2) / 2] + nums2[1 + len(nums2) / 2]) / 2
            else:
                return nums2[(len(nums2) - 1) / 2]
        if not nums2:
            if len(nums1) % 2 == 0:
                return (nums1[len(nums1) / 2] + nums2[1 + len(nums1) / 2]) / 2
            else:
                return nums1[(len(nums1) - 1) / 2]

        left, right = 0, 0
        diff = 0 if (len(nums1) + len(nums2)) % 2 == 0 else 1

        s1, s2 = 0, 0
        e1, e2 = len(nums1) - 1, len(nums2) - 1
        mid1, mid2 = int((e1 - s1) / 2), int((e2 - s2) / 2)
        if nums1[mid1] > nums2[mid2]:
            right += mid1
            s1 = mid1 + 1
            left += mid2
            e2 = mid2 - 1

        elif nums1[mid1] < nums2[mid2]:
            right += mid2
            s2 = mid2 + 1
            left += mid1
            e1 = mid1 - 1

        else:
            if (len(nums1)) % 2 == 0 and (len(nums1)) % 2 == 0:
                return min((nums1[mid1] + nums2[mid2 + 1]) / 2, (nums2[mid2] + nums1[mid1 + 1]) / 2)
            else:
                return (nums1[mid1] + nums2[mid2]) / 2
        print(mid1, s1, e1)
        print(mid2, s2, e2)
        while abs(left - right) > diff:
            mid1, mid2 = int((e1 - s1) / 2), int((e2 - s2) / 2)
            if nums1[mid1] > nums2[mid2]:
                right += mid1
                s1 = mid1 + 1
                left += mid2
                e2 = mid2 - 1

            elif nums1[mid1] < nums2[mid2]:
                right += mid2
                s2 = mid2 + 1
                left += mid1
                e1 = mid1 - 1

            if e1 < s1 or e2 < s2:
                break

        if abs(left - right) > diff:
            if e1 < s1:
                return mid2 + right - left

            if e2 < s2:
                return mid1 + right - left

        # if (len(nums1))%2==0 and (len(nums1))%2==0:
        #     return min((nums1[mid1]+nums2[mid2+1])/2,(nums2[mid2]+nums1[mid1+1])/2)
        else:
            return (nums1[mid1] + nums2[mid2]) / 2


a = [1, 3]
b = [2]
s = Solution()
print(s.findMedianSortedArrays(a, b))
