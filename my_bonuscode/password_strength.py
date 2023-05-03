# ---- Dictionary intro ----

while True:

    password_input = input("Password: ")

    password = {}

    length = False
    digit = False
    upper = False
    lower = False
    symbol = False


    if len(password_input) >= 8:
        length = True
    password["length"] = length


    if any(char.isdigit() for char in password_input):
        digit = True
    password["digit"] = digit

    if any(char.isupper() for char in password_input):
        upper = True
    password["upper"] = upper

    if any(char.islower() for char in password_input):
        lower = True
    password["lower"] = lower

    if any(not char.isalnum() for char in password_input):
        symbol = True
    password["symbol"] = symbol

    print(password)

    if all(password.values()):
        print("Strong password.")
    else:
        print("Weak password.")

