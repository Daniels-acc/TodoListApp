# string decoupling

feet_inch = input("Enter feet and inches: ")


def convert(user_arg):
    index_error_message = "Please provide two arguments: feet and inches."

    try:
        parts = user_arg.split(" ")
        parts = [string.replace(",", ".") for string in parts]

        feet = float(parts[0])
        inch = float(parts[1])

        meters = (feet*0.3048) + (inch*0.0254)
        meters = meters.__round__(3)
        return f"{feet} feet and {inch} inches = {meters} meters"
    except IndexError:
        return index_error_message


print(convert(feet_inch))