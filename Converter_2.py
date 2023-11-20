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

            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()


def unit_check(question):
    # distance lists
    cm = ["cm", "centimeters", "centimeter"]
    m = ["m", "meters", "meter"]
    mm = ["mm", "millimeters", "millimetres"]
    km = ["kilometers", "kilometres", "km"]

    # weight lists
    g = ["grams", "g"]
    kg = ["kilograms", "kg"]
    mg = ["mg", "milligrams"]

    # time lists
    secs = ["seconds", "sec", "secs"]
    mins = ["minutes", "min", "mins"]
    hrs = ["hours", "hrs", "hr"]

    valid = False
    while not valid:

        response = input(question).lower()

        if response in cm:
            return "cm"

        elif response in m:
            return "m"

        elif response in mm:
            return "mm"

        elif response in km:
            return "km"

        else:
            print("Please choose a the unit of distance you are converting to, being Centimeters/Centimetres, Meters/"
                  "Metres, or Kilometers/Kilometres")
            print()

        if response in g:
            return "g"

        elif response in kg:
            return "kg"

        elif response in mg:
            return "mg"

        else:
            print("Please choose a the unit of distance you are converting to, being Milligrams, Grams, "
                  "Kilograms")
            print()

        if response in secs:
            return "secs"

        elif response in mins:
            return "mins"

        elif response in hrs:
            return "hrs"

        else:
            print("Please choose a the unit of distance you are converting to, being Seconds, Minutes, Hours")
            print()


def twd(question):
    valid = False
    while not valid:

        response = input(question)

        if response == "d" or response == "distance":
            return "distance"

        if response == "t" or response == "time":
            return "time"

        if response == "w" or response == "weight":
            return "weight"

        else:
            print("Please provide a either Time, Weight or Distance as a unit")
            print()


def weight_bits():
    print()
    to_be_converted = unit_check_weight(
        "Enter the unit of weight you are converting, being Milligrams, Grams, Kilograms: ")
    print()

    to_be_converted_to = unit_check_weight("Enter the unit of weight you are converting into, being Milligrams, Grams, "
                                           "Kilograms: ")

    print()

    first_part = ("{} to {}".format(to_be_converted, to_be_converted_to))
    output = ("You have chosen {}".format(first_part))
    print(output)

    print()

    to_be_converted_integer = num_check(
        "Enter the integer of the unit you are converting, being more than 0: ")


def distance_bits():

    from_unit = unit_check("What unit do you have? ")
    if from_unit == cm or from_unit == km or from_unit == m or from_unit == mm:
        return print("right")
    else:
        print("wrong ")

    to_unit = unit_check("What unit do you want? ")

    how_much = num_check("How many {} do you have?".format(from_unit))

    print()

    first_part = ("{} to {}".format(from_unit, to_unit))
    output = ("You have chosen {}".format(first_part))
    print(output)

    print(how_much)

    print()

    to_be_converted_integer = num_check(
        "Enter the integer of the unit you are converting, being more than 0: ")


def time_bits():
    print()
    to_be_converted = unit_check_time(
        "Enter the unit of time you are converting, being Seconds, Minutes, Hours: ")
    print()

    to_be_converted_to = unit_check_time("Enter the unit of time you are converting into, being Seconds, Minutes, "
                                         "Hours: ")

    print()

    first_part = ("{} to {}".format(to_be_converted, to_be_converted_to))
    output = ("You have chosen {}".format(first_part))
    print(output)

    print()

    to_be_converted_integer = num_check(
        "Enter the integer of the unit you are converting, being more than 0: ")


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


# Main routine starts here

# Lists to check that chosen units are in the same domain
all_distance = ["mm", "cm", "m", "km"]
all_time = ["secs", "mins", "hrs"]
all_weight = ["g"]

statement_generator("Converter Of Time, Weight and Distance", "+")

first_time = input("Press <enter> to see the instructions or any key to continue")
if first_time == "":
    instructions()

keep_going = ""
while keep_going == "":
    print()
    data_type = twd("What are converting - Weight, Time or Distance (d/ t/ w)?: ")
    if data_type == "weight":
        weight_bits()
    if data_type == "time":
        time_bits()
    elif data_type == "distance":
        distance_bits()
    else:
        print("wrong")

    keep_going = input("Press <enter> to continue or any key to quit ")
    print()

print()
print("Thanks for using the Converter Of Time, Weight and Distance")
print()
