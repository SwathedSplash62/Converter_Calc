def unit_check(question):
    valid = False
    while not valid:

        response = input("What is your chosen unit? - Weight, Time or Distance: ")

        if response == "time" or response == "t" or response == "Time":
            return "You Have Chosen Time"

        elif response == "distance" or response == "d" or response == "Distance":
            return "You Have Chosen Distance"

        elif response == "weight" or response == "w" or response == "Weight":
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

        if response == "km" or response == "kilometers" or response == "Kilometers" or response == "Km" or response == \
                "Kilometres" or response == "kilometres":
            return "Kilometers"

        elif response == "cm" or response == "centimeters" or response == "Centimeters" or response == "Cm" or response\
            \
                == "Centimetres" or response == "centimetres":
            return "Centimeters"

        elif response == "m" or response == "meters" or response == "M" or response == "Meters" or response == "metres"\
        \
                or response == "Metres":
            return "Meters"

        else:
            print("Please choose a the unit of distance you are converting to, being Centimeters/Centimetres, Meters/"
                  "Metres, or Kilometers/Kilometres")
            print()


def unit_check_weight(question):
    valid = False
    while not valid:

        response = input(question)

        if response == "grams" or response == "g" or response == "G" or response == "Grams":
            return "Grams"

        elif response == "milligrams" or response == "mg" or response == "Mg" or response == "Milligrams":
            return "Milligrams"

        elif response == "kilograms" or response == "kg" or response == "Kilograms" or response == "Kg":
            return "Kilograms"

        else:
            print("Please choose a the unit of distance you are converting to, being Milligrams, Grams, "
                  "Kilograms")
            print()


def unit_check_time(question):
    valid = False
    while not valid:

        response = input(question)

        if response == "sec" or response == "seconds" or response == "Sec" or response == "Seconds":
            return "Seconds"

        elif response == "min" or response == "minutes" or response == "Minutes" or response == "Min":
            return "Minutes"

        elif response == "hrs" or response == "hours" or response == "Hours" or response == "Hrs":
            return "Hours"

        else:
            print("Please choose a the unit of distance you are converting to, being Seconds, Minutes "
                  "Hours")
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

    good = True
    while good:

        if output == "You have chosen Seconds to Seconds":
            print("{} Seconds = {} Seconds".format(to_be_converted_integer, to_be_converted_integer))

        if output == "You have chosen Minutes to Minutes":
            print("{} Minutes = {} Minutes".format(to_be_converted_integer, to_be_converted_integer))

        if output == "You have chosen Hours to Hours":
            print("{} Hours = {} Hours".format(to_be_converted_integer, to_be_converted_integer))

        elif output == "You have chosen Seconds to Minutes":
            answer = to_be_converted_integer / 60
            print("{} Seconds = {} Minutes".format(to_be_converted_integer, answer))

        elif output == "You have chosen Minutes to Seconds":
            answer = to_be_converted_integer * 60
            print("{} Minutes = {} Seconds".format(to_be_converted_integer, answer))

        elif output == "You have chosen Minutes to Hours":
            answer = to_be_converted_integer / 60
            print("{} Minutes = {} Hours".format(to_be_converted_integer, answer))

        elif output == "You have chosen Hours to Minutes":
            answer = to_be_converted_integer * 60
            print("{} Hours = {} Minutes".format(to_be_converted_integer, answer))

        elif output == "You have chosen Seconds to Hours":
            answer = to_be_converted_integer / 3600
            print("{} Seconds to {} Hours".format(to_be_converted_integer, answer))

        elif output == "You have chosen Hours to Seconds":
            answer = to_be_converted_integer * 3600
            print("{} Hours = {} Seconds".format(to_be_converted_integer, answer))

        elif output == "You have chosen Hours to Minutes":
            answer = to_be_converted_integer * 60
            print("{} Hours = {} Minutes".format(to_be_converted_integer, answer, ))

        elif output == "You have chosen Minutes to Hours":
            answer = to_be_converted_integer / 60
            print("{} Minutes = {} Hours".format(to_be_converted_integer, answer))

        return ""


def distance_bits():
    print()
    to_be_converted = unit_check_distance(
        "Enter the unit of Distance you are converting being Centimeters/Centimetres, Meters/Metres, Kilometers/"
        "Kilometres: ")
    print()

    to_be_converted_to = unit_check_distance(
        "Enter the unit of Distance you are converting into being Centimeters/Centimetres, Meters/Metres, "
        "Kilometers/Kilometres: ")

    print()

    first_part = ("{} to {}".format(to_be_converted, to_be_converted_to))
    output = ("You have chosen {}".format(first_part))
    print(output)

    print()

    to_be_converted_integer = num_check(
        "Enter the integer of the unit you are converting, being more than 0: ")

    good = True
    while good:

        if output == "You have chosen Centimeters/Centimetres to Centimeters/Centimetres":
            print("{} Centimeters/Centimetres = {} Centimeters/Centimetres".format(to_be_converted_integer,
                                                                                   to_be_converted_integer))
        if output == "You have chosen Meters/Metres to Meters/Metres":
            print("{} Meters/Metres = {} Meters/Metres".format(to_be_converted_integer, to_be_converted_integer))
        if output == "You have chosen Kilometers/Kilometres to Kilometers/Kilometres":
            print("{} Kilometers/Kilometres = {} Kilometers/Kilometres".format(to_be_converted_integer,
                                                                               to_be_converted_integer))
        elif output == "You have chosen Centimeters/Centimetres to Meters/Metres":
            answer = to_be_converted_integer / 100
            print("{} Centimeters/Centimetres = {} Meters/Metres".format(to_be_converted_integer, answer))

        elif output == "You have chosen Meters/Metres to Centimeters/Centimetres":
            answer = to_be_converted_integer * 100
            print("{} Meters/Metres = {} Centimeters/Centimetres".format(to_be_converted_integer, answer))

        elif output == "You have chosen Meters/Metres to Kilometers/Kilometres":
            answer = to_be_converted_integer / 1000
            print("{} Meters/Metres = {} Kilometers/Kilometres".format(to_be_converted_integer, answer))

        elif output == "You have chosen Kilometers/Kilometres to Meters/Metres":
            answer = to_be_converted_integer * 1000
            print("{} Kilometers/Kilometres = {} Meters/Metres".format(to_be_converted_integer, answer))

        elif output == "You have chosen Centimeters/Centimetres to Kilometers/Kilometres":
            answer = to_be_converted_integer / 100000
            print("{} Centimeters/Centimetres to {} Kilometers/Kilometres".format(to_be_converted_integer, answer))

        elif output == "You have chosen Kilometers/Kilometres to Centimeters/Centimetres":
            answer = to_be_converted_integer * 100000
            print("{} Kilometers/kilometres = {} Centimeters/Centimetres".format(to_be_converted_integer, answer))

        elif output == "You have chosen Meters/Metres to Kilometers/Kilometres":
            answer = to_be_converted_integer / 1000
            print("{} Meters/Metres to {} Kilometers/Kilometres".format(to_be_converted_integer, answer))

        elif output == "You have chosen Kilometers/Kilometres to Meters/Metres":
            answer = to_be_converted_integer * 1000
            print("{} Kilometers/Kilometres = {} Meters/Metres".format(to_be_converted_integer, answer))

        return ""


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

    good = True
    while good:

        if output == "You have chosen Grams to Grams":
            print("{} Grams = {} Grams".format(to_be_converted_integer, to_be_converted_integer))

        if output == "You have chosen Milligrams to Milligrams":
            print("{} Milligrams = {} Milligrams".format(to_be_converted_integer, to_be_converted_integer))

        if output == "You have chosen Kilograms to Kilograms":
            print("{} Kilograms = {} Kilograms".format(to_be_converted_integer, to_be_converted_integer))

        elif output == "You have chosen Milligrams to Grams":
            answer = to_be_converted_integer / 10
            print("{} Milligrams = {} Grams".format(to_be_converted_integer, answer))

        elif output == "You have chosen Grams to Milligrams":
            answer = to_be_converted_integer / 100
            print("{} Grams = {} Milligrams".format(to_be_converted_integer, answer))

        elif output == "You have chosen Grams to Kilograms":
            answer = to_be_converted_integer / 1000
            print("{} Grams = {} Kilograms".format(to_be_converted_integer, answer))

        elif output == "You have chosen Kilograms to Grams":
            answer = to_be_converted_integer * 1000
            print("{} Kilograms = {} Grams".format(to_be_converted_integer, answer))

        elif output == "You have chosen Milligrams to Kilograms":
            answer = to_be_converted_integer / 1000000
            print("{} Milligrams to {} Kilograms".format(to_be_converted_integer, answer))

        elif output == "You have chosen Kilograms to Milligrams":
            answer = to_be_converted_integer * 1000000
            print("{} Kilograms = {} Milligrams".format(to_be_converted_integer, answer))

        elif output == "You have chosen Grams to Kilograms":
            answer = to_be_converted_integer / 1000
            print("{} Grams to {} Kilograms".format(to_be_converted_integer, answer))

        elif output == "You have chosen Kilograms to Grams":
            answer = to_be_converted_integer * 1000
            print("{} Kilograms = {} Grams".format(to_be_converted_integer, answer))

        return ""


statement_generator("Converter Of Time, Weight and Distance", "+")

first_time = input("Press <enter> to see the instructions or any key to continue")
if first_time == "":
    instructions()

keep_going = ""
while keep_going == "":
    data_type = unit_check("What is your chosen unit? - Weight, Time or Distance?: ")
    print(data_type)

    if data_type == "You Have Chosen Distance":
        distance_bits()

    if data_type == "You Have Chosen Weight":
        time_bits()

    else:
        time_bits()

    keep_going = input("Press <enter> to continue or any key to quit ")
    print()

print()
print("Thanks for using the Converter Of Time, Weight and Distance")
print()
