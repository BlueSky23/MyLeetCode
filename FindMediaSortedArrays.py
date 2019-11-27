class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if not nums1 and not nums2:
            return -1
        if not nums1:  # nums1 为空
            mid2 = int((len(nums2) - 1) / 2)
            if len(nums2) % 2 == 0:  # 偶数个元素
                return (nums2[mid2] + nums2[mid2 + 1]) / 2
            else:  # 奇数个元素
                return nums2[mid2]
        if not nums2:  # nums2 为空
            mid1 = int((len(nums1) - 1) / 2)
            if len(nums1) % 2 == 0:  # 偶数个元素
                return (nums1[mid1] + nums1[mid1 + 1]) / 2
            else:  # 奇数个元素
                return nums1[mid1]

            # 利用各个数组的中位数逐步排除一半元素
            # 大于2，因为2个元素的数组，依据比中位数的方法不能排除不相关元素
        while (len(nums1) > 2 and len(nums2) > 2):
            mid1 = int((len(nums1) - 1) / 2)
            mid2 = int((len(nums2) - 1) / 2)
            mid = min(mid1, mid2)
            # 依据中位数的大小，排除数组中的不相关元素
            if nums1[mid1] > nums2[mid2]:
                nums1 = nums1[:len(nums1) - mid]
                nums2 = nums2[mid:]
            elif nums1[mid1] < nums2[mid2]:
                nums2 = nums2[:len(nums2) - mid]
                nums1 = nums1[mid:]
            # 两个中位数相等，可以直接得到最终的中位数
            else:
                if len(nums1) % 2 == 0 and len(nums2) % 2 == 0:
                    temp = min(nums1[mid1 + 1], nums2[mid2 + 1])
                    return (nums1[mid] + temp) / 2
                elif len(nums1) % 2 == 1 and len(nums2) % 2 == 1:
                    return (nums1[mid] + nums2[mid]) / 2
                else:
                    return nums1[mid1]

        if len(nums1) < len(nums2):
            short_list = nums1
            long_list = nums2
        else:
            short_list = nums2
            long_list = nums1
            # 将较少列表元素插入较大得列表元素
        idx = 0
        if len(short_list) <= 2:
            for n in short_list:
                if n > long_list[-1]:
                    long_list.append(n)
                else:
                    idx = self.findIndexOfFirstLarger(n, idx, long_list)
                    long_list.insert(idx, n)
            mid = int((len(long_list) - 1) / 2)
            if len(long_list) % 2 == 0:
                return (long_list[mid] + long_list[mid + 1]) / 2
            else:
                return long_list[mid]

    # 用二分法在nums里找到第一个比num大得元素
    def findIndexOfFirstLarger(self, num, idx, nums):
        mid = int((len(nums) - 1) / 2)
        s = max(mid - 3, idx)
        e = min(mid + 3, len(nums) - 1)
        while (s < e):
            mid = int((e + s) / 2)
            if num < nums[mid]:
                e = mid - 1
            elif num > nums[mid]:
                s = mid + 1
            else:
                return mid
        if nums[s] < num:
            return s + 1
        else:
            return s


a = [1, 2]
b = [3, 4]
s = Solution()
print(s.findMedianSortedArrays(a, b))
