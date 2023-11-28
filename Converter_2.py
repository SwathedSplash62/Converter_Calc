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


def distance_unit_check(question):
    # distance lists
    cm = ["cm", "centimeters", "centimeter"]
    m = ["m", "meters", "meter"]
    mm = ["mm", "millimeters", "millimetres"]
    km = ["kilometers", "kilometres", "km"]

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


def weight_unit_check(question):
    # weight lists
    g = ["grams", "g"]
    kg = ["kilograms", "kg"]
    mg = ["mg", "milligrams"]

    valid = False
    while not valid:

        response = input(question).lower()

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


def time_unit_check(question):
    # time lists
    secs = ["seconds", "sec", "secs"]
    mins = ["minutes", "min", "mins"]
    hrs = ["hours", "hrs", "hr"]

    valid = False
    while not valid:

        response = input(question).lower()

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
    response = weight_unit_check("What is your unit?: ").lower()
    if response == "g":
        g()
    if response == "kg":
        kg()
    elif response == "mg":
        mg()


def g():
    how_much = num_check("How much g do you have?")

    output = weight_unit_check("What are you trying to convert {}g to?: ".format(how_much))

    if output == "g":
        final = how_much * 1
        print("{}g to g = {}g".format(how_much, final))
    if output == "kg":
        final = how_much / 1000
        print("{}g to kg = {}kg".format(how_much, final))
    elif output == "mg":
        final = how_much * 1000
        print("{}g to mg = {}mg".format(how_much, final))


def kg():
    how_much = num_check("How much kg do you have?")

    output = weight_unit_check("What are you trying to convert {}kg to?: ".format(how_much))

    if output == "g":
        final = how_much * 1000
        print("{}kg to g = {}g".format(how_much, final))
    if output == "kg":
        final = how_much * 1
        print("{}kg to kg = {}kg".format(how_much, final))
    elif output == "mg":
        final = how_much * 1000000
        print("{}kg to mg = {}mg".format(how_much, final))


def mg():
    how_much = num_check("How much mg do you have?")

    output = weight_unit_check("What are you trying to convert {}mg to?: ".format(how_much))

    if output == "g":
        final = how_much / 1000
        print("{}mg to g = {}g".format(how_much, final))
    if output == "kg":
        final = how_much / 1000000
        print("{}mg to kg = {}kg".format(how_much, final))
    elif output == "mg":
        final = how_much * 1
        print("{}mg to mg = {}mg".format(how_much, final))


def distance_bits():
    response = distance_unit_check("What is your unit?: ").lower()
    if response == "km":
        km()
    if response == "cm":
        cm()
    if response == "mm":
        mm()
    elif response == "m":
        m()


def km():
    how_much = num_check("How much km do you have?")

    output = distance_unit_check("What are you trying to convert {}km to?: ".format(how_much))

    if output == "m":
        final = how_much * 1000
        print("{}km to m = {}km".format(how_much, final))
    if output == "km":
        final = how_much * 1
        print("{}km to km = {}km".format(how_much, final))
    if output == "cm":
        final = how_much * 100000
        print("{}km to cm = {}cm".format(how_much, final))
    elif output == "mm":
        final = how_much * 100000
        print("{}km to mm = {}mm".format(how_much, final))


def m():
    how_much = num_check("How much m do you have?")

    output = distance_unit_check("What are you trying to convert {}m to?: ".format(how_much))

    if output == "m":
        final = how_much * 1
        print("{}m to m = {}m".format(how_much, final))
    if output == "km":
        final = how_much / 1000
        print("{}m to km = {}km".format(how_much, final))
    if output == "cm":
        final = how_much * 100
        print("{}m to cm = {}cm".format(how_much, final))
    elif output == "mm":
        final = how_much * 1000
        print("{}m to mm = {}mm".format(how_much, final))


def cm():
    how_much = num_check("How much cm do you have?")

    output = distance_unit_check("What are you trying to convert {}cm to?: ".format(how_much))

    if output == "m":
        final = how_much / 100
        print("{}cm to m = {}m".format(how_much, final))
    if output == "km":
        final = how_much / 100000
        print("{}cm to km = {}km".format(how_much, final))
    if output == "cm":
        final = how_much * 1
        print("{}cm to cm = {}cm".format(how_much, final))
    elif output == "mm":
        final = how_much * 10
        print("{}cm to mm = {}mm".format(how_much, final))


def mm():
    how_much = num_check("How much mm do you have?")

    output = distance_unit_check("What are you trying to convert {}mm to?: ".format(how_much))

    if output == "mm":
        final = how_much / 1000
        print("{}mm to m = {}m".format(how_much, final))
    if output == "km":
        final = how_much / 1000000
        print("{}mm to km = {}km".format(how_much, final))
    if output == "cm":
        final = how_much * 10
        print("{}mm to cm = {}cm".format(how_much, final))
    elif output == "mm":
        final = how_much * 1
        print("{}mm to mm = {}mm".format(how_much, final))


def time_bits():
    response = time_unit_check("What is your unit?: ").lower()
    if response == "secs":
        secs()
    if response == "mins":
        mins()
    elif response == "hrs":
        hrs()


def secs():
    how_much = num_check("How many secs do you have?")

    output = time_unit_check("What are you trying to convert {}secs to?: ".format(how_much))

    if output == "secs":
        final = how_much * 1
        print("{}secs to secs = {}secs".format(how_much, final))
    if output == "mins":
        final = how_much / 60
        print("{}secs to mins = {}mins".format(how_much, final))
    elif output == "hrs":
        final = how_much / 3600
        print("{}secs to hrs = {}hrs".format(how_much, final))


def mins():
    how_much = num_check("How many mins do you have?")

    output = time_unit_check("What are you trying to convert {}mins to?: ".format(how_much))

    if output == "secs":
        final = how_much * 60
        print("{}mins to secs = {}secs".format(how_much, final))
    if output == "mins":
        final = how_much * 1
        print("{}mins to mins = {}mins".format(how_much, final))
    elif output == "hrs":
        final = how_much / 60
        print("{}mins to hrs = {}hrs".format(how_much, final))


def hrs():
    how_much = num_check("How many hrs do you have?")

    output = time_unit_check("What are you trying to convert {}hrs to?: ".format(how_much))

    if output == "secs":
        final = how_much * 3600
        print("{}hrs to secs = {}secs".format(how_much, final))
    if output == "mins":
        final = how_much * 60
        print("{}hrs to mins = {}mins".format(how_much, final))
    elif output == "hrs":
        final = how_much * 1
        print("{}hrs to hrs = {}hrs".format(how_much, final))


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

    keep_going = input("Press <enter> to continue or any key to quit ")
    print()

print()
print("Thanks for using the Converter Of Time, Weight and Distance")
print()
