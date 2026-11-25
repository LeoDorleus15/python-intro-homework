numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]


def find_min(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest


def find_max(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


def search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1


def bubble_sort(numbers):
    result = list(numbers)
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(result) - 1):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True
    return result


def show_menu():
    print("\n=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    return input("Choose an option (1-5): ").strip()


def main():
    while True:
        choice = show_menu()
        if choice == "1":
            print("Minimum:", find_min(numbers))
        elif choice == "2":
            print("Maximum:", find_max(numbers))
        elif choice == "3":
            target = int(input("Enter a number to search for: "))
            index = search(numbers, target)
            if index != -1:
                print(f"Found at index {index}")
            else:
                print("Not found")
        elif choice == "4":
            print("Sorted list:", bubble_sort(numbers))
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Pick 1-5.")


main()