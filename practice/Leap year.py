while True:
    try:
        year = int(input("Enter a year: "))

        if year % 4 == 0:
            print("This is a leap year")
        else:
            print("This is not a leap year")

    except:
        print("Enter a valid input")
        year = int(input("Enter a year: "))

        if year % 4 == 0:
            print("This is not a leap year")
        else:
            print("This is a leap year")