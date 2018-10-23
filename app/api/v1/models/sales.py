sales = []
products = []


class Sale:
    """this initializes sales class methods"""
    def __init__(self, itemName, attendant, quantity, price, productId):
        self.itemName = itemName
        self.quantity = quantity
        self.price = price
        self.id = len(sales)+1
        self.productId = len(products)+1

    def save(self):
        """this saves product data"""
        payload = {
            "id": self.id,
            "Item Name": self.itemName,
            "Price": self.price,
            "quantity": self.quantity,
            "product id": self.productId
            }
        sales.append(payload)
