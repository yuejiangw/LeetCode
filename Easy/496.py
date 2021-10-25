class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        max_num2 = max(nums2)
        len_num2 = len(nums2)
        res = []
        for num in nums1:
            if num == max_num2:
                res.append(-1)
            else:
                idx = nums2.index(num)
                flag = False
                for i in range(idx, len_num2):
                    if nums2[i] > num:
                        res.append(nums2[i])
                        flag = True
                        break
                if not flag:
                    res.append(-1)
        return res