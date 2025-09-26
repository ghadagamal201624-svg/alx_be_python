def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
    if choice == '1':
        item = input("Enter the item to add: ").strip()
        if item:
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.")
        else:
            print("Item name cannot be empty!")
                
    elif choice == '2':
        if not shopping_list:
            print("Your shopping list is empty!")
        else:
            print("Current shopping list:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
                
            item_to_remove = input("Enter the item to remove: ").strip()
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' has been removed from your shopping list.")
            else:
                print(f"'{item_to_remove}' was not found in your shopping list.")
                    
    elif choice == '3':
            # Display the shopping list
        if not shopping_list:
            print("Your shopping list is empty!")
        else:
            print("\nYour Shopping List:")
            print("-" * 20)
            for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                    print(f"Total items: {len(shopping_list)}")
                
    elif choice == '4':
            # Exit the program
            print("Thank you for using Shopping List Manager. Goodbye!")        
    else:            print("Invalid choice. Please enter a number between 1 and 4.")
if __name__ == "__main__":
    main()
    