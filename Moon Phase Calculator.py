input("Welcome to The Moon Phase Calculator! Press Enter To Continue.")

def parameters(date, month, year):
    if year < 2017 or month > 12 or month < 1 or date > 31 or date < 1:
        print("Error: DATE; between 1 and 31, MONTH; between 1 and 12, YEAR; more than 2017.")
    else:
        calculations(date, month, year)


def calculations(date, month, year):
    a = year / 100
    b = a / 4
    c = 2 - a + b
    e = 365.25 * (year + 4716)
    f = 30.6001 * (month + 1)
    jd = (c + date + e + f) - 1524.5

    days_since_new = jd - 2451549.5
    new_moons = days_since_new / 29.53
    number_dec = new_moons - int(new_moons)
    days_into_cycle = int(number_dec * 29.53)
    display(days_into_cycle)


def display(days_into_cycle):
    if days_into_cycle == 0:
        print("Moon Cycle: New Moon (15 Days Till Full Moon)")
    elif days_into_cycle > 0 or days_into_cycle < 7:
        print("Moon Cycle: Waning Crescent (11 Days Till Full Moon)")
    elif days_into_cycle == 7:
        print("Moon Cycle: Third Quarter (8 Days Till Full Moon)")
    elif days_into_cycle > 7 or days_into_cycle < 15:
        print("Moon Cycle: Waning Gibbous (4 Days Till Full Moon)")
    elif days_into_cycle == 15:
        print("Moon Cycle: Full Moon")
    elif days_into_cycle > 15 or days_into_cycle < 22:
        print("Moon Cycle: Waxing Gibbous (26 Days Till Full Moon)")
    elif days_into_cycle == 22:
        print("Moon Cycle: First Quarter (22 Days Till Full Moon)")
    elif days_into_cycle > 22 or days_into_cycle < 28:
        print("Moon Cycle: Waxing Crescent (18 Days Till Full Moon)")
    elif days_into_cycle == 29:
        print("Moon Cycle: New Moon (15 Days Till Full Moon)")


while True:
    date = int(input("Enter a Date:\n"))
    month = int(input("Enter a Month Number:\n"))
    year = int(input("Enter a Year:\n"))

    parameters(date, month, year)



