distance = float(input("Enter distance in metres: "))
time = int(input("Enter time in seconds: "))


def speed(d, t):
    speed = distance / time
    print(speed, "m/s")


speed(distance, time)

rectangleL = float(input("Enter length in metres: "))
rectangleH = float(input("Enter width in metres: "))
rectangleArea = (rectangleH * 2) + (rectangleL * 2)

circleDiameter = float(input("Enter diameter in metres: "))
radius = circleDiameter / 2
areaCircle = 3.14 * (radius * radius)


def turf():
    amount = rectangleArea - areaCircle
    print(amount, "m of turf needed.")


turf()
