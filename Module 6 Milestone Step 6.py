#Module 6 Milestone step6
# Implement Output shopping cart menu option. Implement Output item's description menu option.
#main menue

        
#class item for storing item name, description, price and quantity
class ItemsToPurchase:
    def __init__(self, item_name: str, item_description : str, item_price :float, item_quantity: int):
        
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(source):
        #print('Is source Item name working', source)
        #print('WHY not',source.item_name)
        #print('Yay')     
        print(source.item_name, source.item_quantity,'@ $',f'{source.item_price:.2f}', '= $', f'{source.item_quantity*source.item_price:.2f}', '\n')
        subtotal = source.item_quantity*source.item_price
        return subtotal
    
    def print_item_description(source):
        print(source.item_name,': ',source.item_description)
    
#class for storing and manipulating shoping cart
class Shopping_Cart:
    def __init__(self ):
        self.customer_name = "none"
        self.current_date = "January 1, 2020"
        self.cart_items = []

    def add_customer_date(self, customer_name, current_date):
        self.customer_name = str(customer_name)
        self.current_date = str(current_date)    
        print(customer_name, current_date)

    def add_items():
        item_to_purchase = 'none'
        while item_to_purchase != '0':
            if item_to_purchase != '0':
                print('What item would you like to add? Enter 0 to exit')
                item_to_purchase = str(input())
                if item_to_purchase == '0':
                    return
                print('What is the discription of ', item_to_purchase)
                description = str(input())
                print('How many ',item_to_purchase, 'are you purchasing?')
                qty = int(input())
                print('What is the price of', item_to_purchase, '?')
                price = float(input())
            
                #creat object 
                item = ItemsToPurchase(item_to_purchase, description, qty, price)
            
                cart.cart_items.append(item)
                print(cart.cart_items)
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
        print('Number of Items:', len(self.cart_items))
        num_items = len(self.cart_items)
        return num_items
        

    #Outputs total of objects in cart.    
    #If cart is empty, output this message: SHOPPING CART IS EMPTY
    def print_total():
        #print('this is print total')
        numcart = cart.get_num_items_in_cart()
        total = 0.0
        for i in range(0, numcart):
            item = cart.cart_items[i]
            print('item is', item)
            subtotal = str(ItemsToPurchase.print_item_cost(item))
            total = float(total) + float(subtotal)
        print('total', total)

    #Outputs each item's description.    
    def print_descriptions():
        print()
        numcart = cart.get_num_items_in_cart()
        for i in range(0, numcart):
            item = cart.cart_items[i]
            #print('item is', item)
            str(ItemsToPurchase.print_item_description(item))

def print_menu(Shoping_Cart):
    while True:
        option = str(input('Menu:\na - Add item to cart\nr - remove item from cart\nc - Change item quantity\ni - Output item description\no - Output shopping cart\nq - Quit\nChose an option:\n'))
    
        if option == 'q':
            print('Quiter')
            return False
        elif option == 'a': 
            Shopping_Cart.add_items()
            
        elif option == 'r':
            print('Removing item from cart')
        
        elif option == 'c':
            print('Changing item quantity')
        
        elif option == 'i':
            print('Output items descripsions')
            print(cart.customer_name,' - ',cart.current_date)
            Shopping_Cart.print_descriptions()
        
        elif option == 'o':
            print('Output shoping cart')
            print(cart.customer_name,' - ',cart.current_date)
            Shopping_Cart.print_total()

        else:
            print("Invalid option try again.")

cart = Shopping_Cart()

print('What is your name?')
name = str(input())
print('What is the date?')
date = str(input())
cart.add_customer_date(name, date)

print_menu(cart)
            


