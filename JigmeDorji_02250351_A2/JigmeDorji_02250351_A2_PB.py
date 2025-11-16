def bubble_sort(names):
    n = len(names)
    sorted_list = names[:]
    for i in range(n - 1):
        for j in range(n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    return sorted_list

def insertion_sort(scores):
    sorted_list = scores[:]
    for i in range(1, len(sorted_list)):
        key = sorted_list[i]
        j = i - 1

        while j >= 0 and sorted_list[j] > key:
            sorted_list[j + 1] = sorted_list[j]
            j -= 1

        sorted_list[j + 1] = key

    return sorted_list

def quick_sort(arr):
    recursive_calls = {"count": 0}

    def _quick_sort(lst):
        recursive_calls["count"] += 1

        if len(lst) <= 1:
            return lst

        pivot = lst[len(lst) // 2]
        left = [x for x in lst if x < pivot]
        middle = [x for x in lst if x == pivot]
        right = [x for x in lst if x > pivot]

        return _quick_sort(left) + middle + _quick_sort(right)

    sorted_list = _quick_sort(arr[:])
    return sorted_list, recursive_calls["count"]

def main():
    student_names = [
        "Kado", "Bobchu", "Zamu", "Nado", "Lemo",
        "Sonam", "Tashi", "Karma", "Dorji", "Chimi",
        "Sangay", "Ugyen", "Dawa", "Phuntsho", "Thinley"
    ]

    test_scores = [78, 45, 92, 67, 88, 54, 73, 82, 91, 59,
                   76, 85, 48, 93, 71, 89, 57, 80, 69, 62]

    book_prices = [450, 230, 678, 125, 890, 345, 760, 510, 299, 455,
                   620, 150, 710, 330, 500]

    print("=== Sorting Algorithms Program ===")

    while True:
        print("\nSelect a sorting operation (1-4):")
        print("1. Bubble Sort - Sort Student Names")
        print("2. Insertion Sort - Sort Test Scores")
        print("3. Quick Sort - Sort Book Prices")
        print("4. Exit program")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nOriginal names:", student_names)
            print("Performing Bubble Sort...")
            sorted_list = bubble_sort(student_names)
            print("Sorted names:", sorted_list)

        elif choice == "2":
            print("\nOriginal scores:", test_scores)
            print("Performing Insertion Sort...")
            sorted_list = insertion_sort(test_scores)
            print("Sorted scores:", sorted_list)

            print("\nTop 5 Scores:")
            top5 = sorted_list[-5:][::-1]
            for i, score in enumerate(top5, 1):
                print(f"{i}. {score}")

        elif choice == "3":
            print("\nOriginal book prices:", book_prices)
            print("Performing Quick Sort...")
            sorted_list, calls = quick_sort(book_prices)
            print("Sorted prices:", sorted_list)
            print(f"Recursive calls made: {calls}")

        elif choice == "4":
            print("Thank you for using the sorting program!")
            break

        else:
            print("Invalid choice! Please enter 1-4.")
            continue

        again = input("\nWould you like to perform another sort? (y/n): ").lower()
        if again != 'y':
            print("Thank you for using the sorting program!")
            break

main()
