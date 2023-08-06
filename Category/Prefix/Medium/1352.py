class ProductOfNumbers:
    def __init__(self):
        # 初始化放一个 1 便于计算后面的乘积
        self.product = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # 如果添加的元素是 0 则前面的积都作废
            self.product.clear()
            self.product.append(1)
        else:
            if len(self.product) == 0:
                self.product.append(num)
            else:
                self.product.append(self.product[-1] * num)

    def getProduct(self, k: int) -> int:
        n = len(self.product)
        # product 中剩的是后面不为 0 元素的积
        if k > n - 1:
            return 0
        return self.product[n - 1] // self.product[n - 1 - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
