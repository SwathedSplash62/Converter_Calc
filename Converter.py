def unit_check(question):
    valid = False
    while not valid:
        error = "Please enter a unit being Weight, Distance or Time "

        try:

            # ask user to enter a number
            response = int(input(question))

            # checks number is more than zero
            if 1 <= response <= 200:
                return response

            # Outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()


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


def user_choice():
    valid = False
    while not valid:

        response = input("What is your chosen unit?: ").lower()

        if response == "time" or response == "t":
            return "You have chosen Time "

        elif response == "distance" or response == "d":
            return "You have chosen Distance"

        elif response == "Weight" or "w":
            return "You have chosen Weight"

        else:
            print("Please choose a valid file type in the form of time, distance or weight")
            print()


def distance_bits():
    print()
    to_be_converted = input("Enter the unit of distance you are converting, being Meters, Centimeters, or Kilometers: ")
    to_be_converted_to = input("Enter the unit of distance you are converting to, being Meters, Centimeters, "
                               "or Kilometers: ")

    print()
    heading = input("{} to {}".format(to_be_converted, to_be_converted_to))
    print()
    statement_generator("You have chosen {}", "+".format(heading))

    return ""


def time_bits():
    print()
    to_be_converted = input("Enter the unit of distance you are converting, being Meters, Centimeters, or Kilometers: ")
    to_be_converted_to = input("Enter the unit of distance you are converting to, being Meters, Centimeters, "
                               "or Kilometers: ")

    print()
    heading = input("{} to {}".format(to_be_converted, to_be_converted_to))
    print()
    statement_generator("You have chosen {}", "+".format(heading))

    return ""


def weight_bits():
    print()
    to_be_converted = input("Enter the unit of distance you are converting, being Meters, Centimeters, or Kilometers: ")
    to_be_converted_to = input("Enter the unit of distance you are converting to, being Meters, Centimeters, "
                               "or Kilometers: ")

    print()
    heading = input("{} to {}".format(to_be_converted, to_be_converted_to))
    print()
    statement_generator("You have chosen {}", "+".format(heading))

    return ""


statement_generator("Converter Of Time, Weight and Distance", "+")

first_time = input("Press <enter> to see the instructions or any key to continue")
if first_time == "":
    instructions()

keep_going = ""
while keep_going == "":

    data_type = user_choice()
    print("You Chose", data_type)

    if data_type == "distance":
        distance_bits()

    elif data_type == "time":
        time_bits()

    else:
        weight_bits()

    print()
    keep_going = input("Press <enter> to continue or any key to quit")

print()
print("Thanks for using the Calculator for Integers, Text & Images")
