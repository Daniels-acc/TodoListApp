# Coding Exercise 1
# Create a function that finds out the state of water (i.e., gas, liquid, solid) given the temperature.
# In other words, the function has a temperature parameter and returns either "Gas",
# "Liquid" or "Solid" as a string depending on the temperature.
# The function should be written in a separate file from the command line interface file.
# The output should look like in the screenshot below:

state_solid = 0
state_gas = 100

def water_state(temp):
    type_error = 'Enter numbers only.'

    try:
        temp = float(temp)
        if temp <= state_solid:
            return 'Solid'
        elif 0 < temp < state_gas:
            return 'Liquid'
        elif temp >= 100:
            return 'Gas'
    except TypeError:
        return type_error
    except ValueError:
        return type_error


water_temp = input('Enter water temperature: ')

print(water_state(water_temp))