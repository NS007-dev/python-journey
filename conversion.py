def convert():
    currentUnits = input("cm or inches?")
    if currentUnits == "inches":
        num = int(input("number: "))
        print(num * 2.54, "cm")
    elif currentUnits == "cm":
        num = int(input("number: "))
        print(num * 0.393700787, "in")
    else:
        print("invalid")


convert()


def cmToIn(num):
    num = int(input("number: "))
    print(num * 0.393700787, "in")


def inToCm(num):
    num = int(input("number: "))
    print(num * 2.54, "cm")


choice = input("current units? cm or in?")
if choice == "cm":
    cmToIn()
elif choice == "in":
    inToCm()
else:
    "invalid"
