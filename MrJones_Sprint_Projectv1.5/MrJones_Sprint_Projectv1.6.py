def multi_table(a):
    for i in range(1, 11):
        print ('{0} x {1} = {2}'.format(a, i, a*i))

if __name__ == '__main__':
    a = input('Please enter a number here: ')
    multi_table(float(a))
    
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