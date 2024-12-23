#Module 6 Milestone step4
class ItemsToPurchase:
    def __init__(self, item_name, item_description, item_price, item_quantity):
        self.item_name = str(item_name)
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
        self.item_description = str(item_description)

    def print_item_cost(self):
        print( self.item_name, self.item_quantity,'@ $',f'{self.item_price:.2f}', '= $', f'{self.item_quantity*self.item_price:.2f}', '\n')

class Shopping_Cart:
    def __init__(self, ):
        self.customer_name = "none"
        self.current_date = "January 1, 2020"
        self.cart_items = []
    def add_customer_date(self, customer_name, current_date):
        self.customer_name = str(customer_name)
        self.current_date = str(current_date)    
        print(customer_name, current_date)

    def add_items(self, item_to_purchase):
        while item_to_purchase != '0':
            if item_to_purchase != '0':
                print('What is the discription of ', item_to_purchase)
                description = str(input())
                print('How many ',item_to_purchase, 'are you purchasing?')
                qty = int(input())
                print('What is the price of', item_to_purchase, '?')
                price = float(input())
            
                #creat class 
                ItemsToPurchase(item_to_purchase, description, qty, price)
            
                self.cart_items.append(item_to_purchase)
                #add more items if desired
                print ('What is the next item to purchase? Enter 0 to exit.')
                item_to_purchase = str(input())
                print(self.cart_items)
        print('Leaving add item')
                    

    def remove_items(self, item_remove):
        for i in range(0, len(self.cart_items)):
            print(self.cart_items[i])
        print("What item would you like to remove")    
        if item_remove in self.cart_items:
            self.cart_items.remove(item_remove)
        else:
            print('Item not found and not removed from list')
        print(self.cart_items)
    
    #Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
    #If item can be found (by name) in cart, check if parameter has default values for description, price, and quantity. If not, modify item in cart.
    #If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
    def modify_item(self, item_to_modify):
        pass
    
    #Returns quantity of all items in cart. Has no parameters.
    def get_num_items_in_cart(self):
        num_items = 0
        print('are working')
        print(num_items)
        print(len(self.cart_items))

    #Determines and returns the total cost of items in cart. Has no parameters.
    def get_cost_of_cart():
        pass

    #Outputs total of objects in cart.    
    #If cart is empty, output this message: SHOPPING CART IS EMPTY
    def print_total():
        pass

    #Outputs each item's description.    
    def print_discriptions():
        pass

cart = Shopping_Cart()

print('What are you wanting to buy?')
item = str(input())
cart.add_items(item)
print('What item do you want to remove?')
remove_item = str(input())
cart.remove_items(remove_item)

            


