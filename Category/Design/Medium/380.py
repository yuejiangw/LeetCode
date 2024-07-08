from random import randint


class RandomizedSet:
    """
    思路: 数组在尾部插入和删除元素的时间复杂度均为O(1)，因此用数组存放所有元素，
    同时用一个哈希表存放各个元素与其对应的数组下标。在删除元素时，将待删除元素与
    数组末尾元素换位置，之后再删除数组末尾元素即可。
    """

    def __init__(self):
        self.nums = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.val_to_index[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        # swap target val with the num at the end of the list
        end_num = self.nums[-1]
        idx1, idx2 = self.val_to_index[val], self.val_to_index[end_num]
        self.nums[idx1] = end_num
        self.val_to_index[end_num] = idx1
        self.nums.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        idx = randint(0, len(self.nums) - 1)
        return self.nums[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
