class FoodItem:
    food_id = 1 
    
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = FoodItem.food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock
        FoodItem.food_id += 1  
        
    def edit_food_item(self, name=None, quantity=None, price=None, discount=None, stock=None):
        if name is not None:
            self.name = name
        if quantity is not None:
            self.quantity = quantity
        if price is not None:
            self.price = price
        if discount is not None:
            self.discount = discount
        if stock is not None:
            self.stock = stock
    
    def __str__(self):
        return f"{self.food_id}: {self.name} ({self.quantity}) - INR {self.price} ({self.discount}% off), {self.stock} left in stock"
food_item_1 = FoodItem("Tandoori Chicken", "4 pieces", 240, 10, 20)
food_item_2 = FoodItem("Vegan Burger", "1 Piece", 320, 5, 15)
food_item_3 = FoodItem("Truffle Cake", "500gm", 900, 15, 10)
food_item_2.edit_food_item(name="Vegan Cheeseburger", price=350, stock=20)
food_items = [food_item_1, food_item_2, food_item_3]
for food_item in food_items:
    print(food_item)
food_items = [food_item for food_item in food_items if food_item.food_id != 1]
class User:
    users = [] 
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        User.users.append(self)  
        
    def update_profile(self, full_name=None, phone_number=None, email=None, address=None, password=None):
        if full_name is not None:
            self.full_name = full_name
        if phone_number is not None:
            self.phone_number = phone_number
        if email is not None:
            self.email = email
        if address is not None:
            self.address = address
        if password is not None:
            self
