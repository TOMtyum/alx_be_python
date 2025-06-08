def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' added to the shopping list.")
            
        elif choice == '2':
            if not shopping_list:
                print("Your shopping list is empty!")
                continue
                
            print("Current items:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
                
            item_to_remove = input("Enter the item name or number to remove: ")
            
            if item_to_remove.isdigit():
                index = int(item_to_remove) - 1
                if 0 <= index < len(shopping_list):
                    removed = shopping_list.pop(index)
                    print(f"Removed '{removed}'")
                else:
                    print("Invalid number!")
            elif item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"Removed '{item_to_remove}'")
            else:
                print(f"'{item_to_remove}' not found!")
                
        elif choice == '3':
            if not shopping_list:
                print("Your shopping list is empty!")
            else:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                    
        elif choice == '4':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()