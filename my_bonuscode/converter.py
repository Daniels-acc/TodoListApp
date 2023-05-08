# string decoupling

feet_inch = input("Enter feet and inches: ")


def convert(user_arg):
    index_error_message = "Please provide two arguments: feet and inches."
    value_error_message = "Please enter numbers only."

    try:
        parts = user_arg.split(" ")
        parts = [string.replace(",", ".") for string in parts]

        feet = float(parts[0])
        inch = float(parts[1])

        meters = (feet*0.3048) + (inch*0.0254)
        meters = meters.__round__(3)
        return meters
    except IndexError:
        return index_error_message
    except ValueError:
        return value_error_message


result: float | str = convert(feet_inch)
#
if not isinstance(result, (int, float)):
    print("Wrong arguments.")
    exit()
elif result < 1.25:
    print("Child height is not enough for the pool slider.")
else:
    print("Child can use the slide.")