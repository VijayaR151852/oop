class Item:
    def __init__(self,name=None,price=0,category=0):
        if(price<=0):
            raise ValueError("Invalid value for price, got {}".format(price))
        self.name=name
        self.price=price
        self.category=category
        
    def __str__(self):
        return f"{self.name}@{self.price}-{self.category}"
        
class Query:
    def __init__(self,fie)