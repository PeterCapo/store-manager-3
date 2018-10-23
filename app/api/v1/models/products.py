from app.api.v1.validators.utils import Validators
products = []


class Product:
    def __init__(
        self, productName,
        price, category,
        stockBalance, minStockBalance
    ):
        self.productName = productName
        self.price = price
        self.id = len(products)+1
        self.category = category
        self.stockBalance = stockBalance
        self.minStockBalance = minStockBalance

    def save(self):
        payload = {
            "id": self.id,
            "Product Name": self.productName,
            "price": self.price,
            "Stock Balance": self.stockBalance,
            "category": self.category,
            "'Minimum Inventory": self.minStockBalance
            }
        products.append(payload)

    def get_id(self, product_id):
        for product in products:
            if product.id == product_id:
                return product
