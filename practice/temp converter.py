"""
This is a temperature converter and can convert F to C and C to F

It basically takes the input (temperature and temp unit(C or F))

Then to convert it we use if statement and if temp type is equal to C or F it will convert it to
the other one

We use this equation for converting C to F
        ((temp/5) * 9) + 32
We use this equation for converting F to C
        ((temp - 32 )* 5) / 9
"""

print("Put C or F in upper case and not in lower case")

# Getting the inputs from the user (the temperature and temperature unit(C or F))
# Temp unit(C or F)
temp_type = input("C or F: ")
# Getting the temperature
temp = float(input("Enter the temperature: "))

# Using if statement to tell the temperature
# If temp unit it C convert it to F and print it
if temp_type == "C":
    # Converting it to F
    temp_convert = ((temp / 5) * 9) + 32
    # Printing the temperature
    print(str(temp_convert) + " F")

# If temp unit is F convert it to C and print it
elif temp_type == "F":
    # Converting it to C
    temp_convert = ((temp - 32) * 5) / 9
    # Printing the temperature
    print(str(temp_convert) + "C")

# If the temperature unit is neither C nor F then displaying this
else:
    print("Invalid temp unit")
    print("Try entering the unit in upper case")
