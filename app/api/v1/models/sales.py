sales = []
products = []


class Sale:
    """this initializes sales class methods"""
    def __init__(self, attendant, quantity, productId):
        self.quantity = quantity
        self.attendant = attendant
        self.id = len(sales)+1
        self.productId = len(products)+1

    def save(self):
        """this saves product data"""
        payload = {
            "id": self.id,
            "attendant": self.attendant,
            "quantity": self.quantity,
            "product id": self.productId
            }
        sales.append(payload)
