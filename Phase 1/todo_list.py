todo_list = ["food", "water", "sleep"]

while True:
    operation = input("Enter an operation (add, remove, show one, show all, exit): ")

    if operation.lower() == "exit":
        break

    elif operation.lower() == "add":
        how_many = int(input("How many items do you want to add? "))
        for _ in range(how_many):
            todo_list.append(input("Enter a value to add: "))

    elif operation.lower() == "remove":
        value = input("Enter a value to remove: ")
        if value in todo_list:
            todo_list.remove(value)
        else:
            print("Item not found in the list.")

    elif operation.lower() == "show one":
        index = int(input("Enter the index to show (starting from 0): "))
        if 0 <= index < len(todo_list):
            print(f"{index} is {todo_list[index]}")
        else:
            print("Invalid index.")

    elif operation.lower() == "show all":
        for i, item in enumerate(todo_list):
            print(f"{i} is {item}")