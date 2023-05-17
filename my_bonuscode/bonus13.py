feet_inches = input("Enter feet and inches: ")

def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet*231 + inches*545