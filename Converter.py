def num_check(question):
    valid = False
    while not valid:
        error = "Please enter an integer that is greater than or equal to one and less than or equal to 200"

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


int(input(user_choice()))
