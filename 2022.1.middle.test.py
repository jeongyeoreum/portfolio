
class Item:
    def __init__(self,name,price):
        self._name = name
        self._price = price
    @property
    def price(self):
        return self._price
class DiscountedItem(Item):
    def __init__(self,name, price, discounted_rate):
        super().__init__(name,price)
        self.__discounted_rate = discounted_rate
    def calculate_price(self):
        return self._price*self.__discounted_rate

if __name__ == '__main__':
    buying_Items = [DiscountedItem('TV',2000,0.3),DiscountedItem('Laptop',1200,0.2)]

    total_price, discounted_price = 0,0
    for item in buying_Items:
        sales_price = item.calculate_price()
        total_price += sales_price
        discounted_price += item.price - sales_price
    print(f'총지불금액; {total_price}')
    print(f'할인총액: {discounted_price}')