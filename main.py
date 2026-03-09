import utils

def menu():
    while True:
        print("\n===== Expense Tracker =====")
        print("0) Update income and goals")
        print("1) Add expense")
        print("2) Delete expense")
        print("3) Monthly Summary")
        print("4) Export data to CSV")
        print("5) Exit")

        choice = input("Select option: ")

        if choice == "0":
            utils.update_income()

        elif choice == "1":
            utils.add_expense()

        elif choice == "2":
            utils.delete_expense()

        elif choice == "3":
            month = input("Enter month (MM): ")
            year = input("Enter year (YYYY): ")
            utils.monthly_summary(month, year)

        elif choice == "4":
            start_m = input("Start month (MM): ")
            start_y = input("Start year (YYYY): ")
            end_m = input("End month (MM): ")
            end_y = input("End year (YYYY): ")
            utils.export_csv(start_m, start_y, end_m, end_y)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    menu()
