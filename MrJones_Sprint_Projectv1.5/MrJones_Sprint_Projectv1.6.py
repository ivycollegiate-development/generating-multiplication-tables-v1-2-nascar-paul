
def main():
    while True:
        try:
            a = float(input('Please enter a number here: '))
            multi_table(a)
        except ValueError:
            print('Invalid input, please enter a number value.')
            continue
        choice = input("Do you want to generate another table? (y/n)").lowwer()
        if choice != 'y':
            print("Thanks for using the multiplication table generator!")
            break
        if __name__ == '__main__':
            main()