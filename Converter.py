def unit_check(question):
    valid = False
    while not valid:

        response = input("What is your chosen unit?: ")

        if response == "time" or response == "t":
            return "You Have Chosen Time"

        elif response == "distance" or response == "d":
            return "You Have Chosen Distance"

        elif response == "weight" or response == "w":
            return "You Have Chosen Weight"

        else:
            print("Please choose a valid unit in the form of Weight, Distance or Time.")
            print()


def num_check(question):
    valid = False
    while not valid:
        error = "Please enter something that is more than zero"

        try:

            # ask user to enter a number
            response = float(input(question))

            # checks number is more than zero
            if response > 0:
                return response
                print(error)
                print()


            # Outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()


def unit_check_distance(question):
    valid = False
    while not valid:

        response = input(question)

        if response == "km" or response == "kilometers":
            return "Kilometers"

        elif response == "cm" or response == "centimeters":
            return "Centimeters"

        elif response == "m" or response == "meters":
            return "Meters"

        else:
            print("Please choose a the unit of distance you are converting to, being Centimeters, Meters, or "
                  "Kilometers")
            print()


def unit_check_weight(question):
    valid = False
    while not valid:

        response = input(question)

        if response == "grams" or response == "g":
            return "Grams"

        elif response == "milligrams" or response == "mg":
            return "Milligrams"

        elif response == "Kilograms" or response == "kg":
            return "Kilograms"

        else:
            print("Please choose a the unit of distance you are converting to, being Milligrams, Grams, "
                  "Kilograms")
            print()


def unit_check_time(question):
    valid = False
    while not valid:

        response = input(question)

        if response == "sec" or response == "seconds":
            return "Seconds"

        elif response == "min" or response == "minutes":
            return "Minutes"

        elif response == "hrs" or response == "hours":
            return "Hours"

        else:
            print("Please choose a the unit of distance you are converting to, being Seconds, Minutes "
                  "Hours")

    return ""


def statement_generator(text, decoration):
    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


def instructions():
    statement_generator("Instructions/information", "-")
    print()
    print("Please choose a number than is greater than or equal to one and less than or equal to 200")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each "
          "calculation or any key to quit.")
    print()
    statement_generator("Converter Of Time, Weight and Distance", "+")
    return ""


def time_bits():
    print()
    to_be_converted = unit_check_time(
        "Enter the unit of time you are converting, being Seconds, Minutes, Hours: ")
    to_be_converted_to = unit_check_time("Enter the unit of time you are converting to, being Seconds, Minutes, "
                                         "Hours: ")

    print("You have chosen {} to {}".format(to_be_converted, to_be_converted_to))
    print()


def distance_bits():
    print()
    to_be_converted = unit_check_distance(
        "Enter the unit of Distance you are converting being Centimeters, Meters, Kilometers: ")
    to_be_converted_to = unit_check_distance(
        "Enter the unit of Distance you are to converting being Centimeters, Meters, Kilometers: ")

    print("You have chosen {} to {}".format(to_be_converted, to_be_converted_to))
    print()


def weight_bits():
    print()
    to_be_converted = unit_check_weight(
        "Enter the unit of weight you are converting, being Milligrams, Grams, Kilograms: ")
    to_be_converted_to = unit_check_weight("Enter the unit of distance you are converting to, being Milligrams, Grams, "
                                           "Kilograms: ")

    first_part = ("{} to {}".format(to_be_converted, to_be_converted_to))
    output =("You have chosen {}".format(first_part))
    print(output)

    print()

    to_be_converted_integer = num_check(
        "Enter the integer of the unit you are converting, being more than 0: ")
    valid = False
    while not valid:

        my_dict = {
            "convert_down": "0.001",
            "convert_up": "1000"
        }

        response = output

        if response == "Grams to Grams":
            return "output"

        elif response == "Grams to Kilograms":
            to_do = input("double or half? ").lower()
            multiply_by = my_dict[to_do]
            answer = to_be_converted_integer * multiply_by
            print("{} x {} = {}".format(to_be_converted_integer, multiply_by, answer))

        elif response == "hrs" or response == "hours":
            return "Hours"

        elif response == "min" or response == "minutes":
            return "Minutes"

        elif response == "hrs" or response == "hours":
            return "Hours"


statement_generator("Converter Of Time, Weight and Distance", "+")

first_time = input("Press <enter> to see the instructions or any key to continue")
if first_time == "":
    instructions()

keep_going = ""
while keep_going == "":
    data_type = unit_check("What is your chosen unit?: ")
    print(data_type)

    if data_type == "You Have Chosen Distance":
        distance_bits()

    elif data_type == "You Have Chosen Time":
        time_bits()

    else:
        weight_bits()

print()
print("Thanks for using the Converter Of Time, Weight and Distance")
