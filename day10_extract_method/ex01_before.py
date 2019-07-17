class Receipt:
    def __init__(self): self.items, self.discounts, self.tax = [], list(), 0.065

    # 计算最终价格的方法中，逻辑太复杂
    def calculate(self):
        total = 0
        total += sum(self.items)
        total -= sum(self.discounts)
        tax = total * self.tax
        total += tax
        return total

if __name__ == '__main__':
    receipt = Receipt()
    receipt.items.extend([10, 20, 30, 40, 50])
    receipt.discounts.extend([2, 4, 6, 8, 10])
    print(receipt.calculate())
