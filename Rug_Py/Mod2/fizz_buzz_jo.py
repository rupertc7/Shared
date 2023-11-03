choice = 'None'
number = 0
while choice != 'y' or choice != 'Y':
    number=input("we are going to play FizzBuzz\nplease type a range number from 0 to... : ")
    if number.isdigit():
        #Get input from the user
        for x in range (0, (int(number) + 1)):
            if x % 3 == 0:
                print("bizz")
            if x % 5 == 0:
                print("buzz")
            else:
                print(x)

    else:
        print("Please enter a valid input ")

        choice = str(input("do you want to exit? y or n \n"))
        if choice == 'y' or choice == 'Y':
                print("the program ends. Thanks")
                exit()