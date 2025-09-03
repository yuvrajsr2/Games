currency_type = input("dollar, rupee, euro: ")
currency_convert = input("What would you like it to convert to: ")
currency = float(input("Enter a number: "))

if currency_type == "dollar":

    if currency_convert == "rupee":
        result = currency * 72.90
        print(result)

    elif currency_convert == "euro":
        result = currency * 0.83
        print(result)

    else:
        print("Put a valid currency to convert like rupee and euro")


if currency_type == "rupee":

    if currency_convert == "dollar":
        result = currency * 0.014
        print(result)

    elif currency_convert == "euro":
        result = currency * 0.011
        print(result)

    else:
        print("Put a valid currency to convert like dollar and euro")


if currency_type == "euro":

    if currency_convert == "dollar":
        result = currency * 1.21
        print(result)

    elif currency_convert == "rupee":
        result = currency * 88.26
        print(result)

    else:
        print("Put a valid currency to convert like dollar and rupee")
