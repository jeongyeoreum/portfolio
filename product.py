

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_price(self):
        return self.price*self.quantity

    def __str__(self):
        return f'{self.name:30s}\t{self.price:5d}원{self.quantity:3d}개'



if __name__ == '__main__':

    products = [Product('제주 삼다수 그린 2L', '1,200', '5'), Product('신라면(120g*5입)', '4,100', '2')
        , Product('CJ햇반(210g*12입)', '13,980', '1'), Product('몽쉘크림(12입)', '4,780', '1')]

    for product in products:
        print(product)
