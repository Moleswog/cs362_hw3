def leapyear(x):
    if (x % 400) == 0:
        print(x, "is a leap year")
    else:
        if ((x % 4) == 0) and ((x % 100) != 0):
            print(x, "is a leap year")
        else:
            print(x, "is NOT a leap year")

def run():
    try:
        val = int(input("Enter a year: "))
        leapyear(val)
    except ValueError:
        print("Please input a number. Try again.")
        run()

run()
input("Press enter to close");
