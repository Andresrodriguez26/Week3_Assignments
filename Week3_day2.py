# Exercise 1 - Turn the shopping cart program from last week into an object-oriented program
# The comments in the cell below are there as a guide for thinking about the problem. However, 
#if you feel a different way is best for you and your own thought process, please do what feels best for you by all means.

class Shop_cart():
    def __init__(self):
        self.shopping_cart = {}

    def add_item(self):
        new_item = input("What item would you like to add? ")
        quantity = int(input("How many? "))
    
        if new_item in self.shopping_cart:
            self.shopping_cart[new_item] += quantity
        else: 
            self.shopping_cart[new_item] = quantity
    
    def delete_item(self):
        deleted = input("What item would you like to delete? ")
        if deleted in self.shopping_cart:
            dele_quant = int(input(f"How many {deleted}(s) would you like to delete? "))
            if dele_quant >= self.shopping_cart[deleted]:
                del self.shopping_cart[deleted]
                print(f"{deleted} removed from your shopping cart.")
            else:
                self.shopping_cart[deleted] -= dele_quant
        else:
            print("That is not in your cart. Please try again")

    def view_store(self):
        print("Here is your current shopping cart:")
        for item, quantity in self.shopping_cart.items():
            print(f"{quantity} {item} (s)")
            
def main_func():
    
    finalcart = Shop_cart()
    
    while True:
        response = input("What would you like to do? add, delete, view ")
    
        if response.lower() == "add":
            finalcart.add_item()
        elif response.lower() == "delete":
            finalcart.delete_item()
        
        elif response.lower() == "view":
            finalcart.view_store()
        
        elif response.lower() == "quit":
            break
        else: 
            print("Please enter a valid response")
        
    if finalcart.shopping_cart:
        print("These are your final items:")
        for item, quantity in finalcart.shopping_cart.items():
            print(f"{quantity} {item}(s)")
    else:
        print("Your shopping cart is empty.")

    print("Thank you for shopping with us!")
   
main_func()

print("\n")

# Exercise 2 
# Write a Python class which has two methods get_String and print_String. get_String accept a 
# string from the user and print_String print the string in upper case

class String():
    def __init__(self):
        self.string_input = ""
        
    def inpt(self):
        self.string_input = input("Please enter a string: ")
        
    def print_string(self):
        print(self.string_input.upper())
        
result = String()
result.inpt()
result.print_string()