class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 问题：该方法 Discount 类使用的更多，应该移动到 Discount 类中
    def get_discount(self):
        return 0.5 if any([self.age <= 6, self.age >= 60]) else 1
class Discount:
    def __init__(self, person): self.__person = person
    def get_money(self, money): return self.__person.get_discount() * money

if __name__ == '__main__':
    p1 = Person('小铭', 18)
    p2 = Person('大蜥蜴', 70)
    print(Discount(p1).get_money(1000))
    print(Discount(p2).get_money(1000))
