def linear_search(student_ids, target):
    comparisons = 0
    for index, value in enumerate(student_ids):
        comparisons += 1
        if value == target:
            return index + 1, comparisons
    return None, comparisons


def binary_search(scores, target):
    left, right = 0, len(scores) - 1
    comparisons = 0

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        if scores[mid] == target:
            return mid + 1, comparisons
        elif target < scores[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return None, comparisons


def main():
    student_ids = [1001, 1005, 1002, 1008, 1003, 1010, 1004, 1009, 1007, 1012,
                   1015, 1011, 1013, 1016, 1006, 1014, 1017, 1018, 1019, 1020]

    scores = [45, 52, 58, 63, 67, 72, 75, 78, 82, 85,
              88, 90, 92, 95, 98, 99, 100, 101, 103, 105]

    print("=== Searching Algorithms Program ===")

    while True:
        print("\nSelect a search operation (1-3):")
        print("1. Linear Search - Find Student ID")
        print("2. Binary Search - Find Score")
        print("3. Exit program")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("\nSearching in the list:", student_ids)
            try:
                target = int(input("Enter Student ID to search: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            pos, comparisons = linear_search(student_ids, target)

            if pos:
                print(f"Result: Student ID {target} found at position {pos}. Comparisons made: {comparisons}")
            else:
                print(f"Result: Student ID not found. Comparisons made: {comparisons}")

        elif choice == "2":
            print("\nSorted scores:", scores)
            try:
                target = int(input("Enter score to search: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            pos, comparisons = binary_search(scores, target)
            if pos:
                print(f"Result: Score {target} found at position {pos}. Comparisons made: {comparisons}")
            else:
                print(f"Result: Score not found. Comparisons made: {comparisons}")

        elif choice == "3":
            print("Thanks for using the search program!")
            break

        else:
            print("Invalid choice! Please enter 1-3.")
            continue

        again = input("\nWould you like to perform another search? (y/n): ").lower()
        if again != 'y':
            print("Thanks for using the search program!")
            break

main()
