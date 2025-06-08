def display_menu():
    """Display the main menu options."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function to run the shopping list manager."""
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            # Add item functionality
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' added to the shopping list.")
            else:
                print("No item entered. Please try again.")
                
        elif choice == '2':
            # Remove item functionality
            if not shopping_list:
                print("Your shopping list is empty!")
                continue
                
            print("Current items in your list:")
            for index, item in enumerate(shopping_list, start=1):
                print(f"{index}. {item}")
                
            item_to_remove = input("Enter the item name or number to remove: ").strip()
            
            try:
                # Try to remove by index if input is a number
                item_num = int(item_to_remove)
                if 1 <= item_num <= len(shopping_list):
                    removed_item = shopping_list.pop(item_num - 1)
                    print(f"'{removed_item}' removed from the shopping list.")
                else:
                    print("Invalid item number.")
            except ValueError:
                # Remove by name if input isn't a number
                if item_to_remove in shopping_list:
                    shopping_list.remove(item_to_remove)
                    print(f"'{item_to_remove}' removed from the shopping list.")
                else:
                    print(f"'{item_to_remove}' not found in the shopping list.")
                    
        elif choice == '3':
            # View list functionality
            if not shopping_list:
            