import math
from Values import Values
from Uncertainties import *

# this is the file that deals with a user interface. When we are finished we'll make this file Main.py file.


# global variables dictionary
variables = {}


def set_variable_name(var_name, value):
    # variables[name] = value
    variables.update({var_name: value})
    # eval("variables[" + str(var_name) + "] = " + str(value))


def get_variable_name(str_in):
    # everything before the equals sign
    variable_name = str_in.split("=")[0].strip().replace(' ', '_')
    return variable_name


def get_definition_body(str_in):
    # everything after the equals sign lmao
    definition_body = str_in.split("=")[1].strip()
    return definition_body


def get_actual_value(str_in):
    # gets everything before the plus sign
    actual_value = str_in.split("+")[0].strip()
    return actual_value


def get_uncertainty_value(str_in):
    # everything after the plus sign
    return str_in.split("+")[1].strip()

# this is used for detecting variable definitions


def is_num_definition(str_in):
    # if the definition is in the format m = a + b, where a and b are both Values
    try:
        string_test = str_in.replace('+', '').replace(' ', '').replace('.', '')
        print("string test " + string_test)
        return string_test.isdigit()
    except IndexError:
        # is there aren't any spaces or dots or plus signs
        return False


print("> Set a variable or type out an equation.")
print("> To set a variable in absolute uncertainty form please type it out in the format m = 50 + 0.05 where m is the variable name, 50 is the value, and 0.05 is the absolute uncertainty.")
print("please note any spaces in variable names will be replaced with an underscore")


def main():
    input_string = input(">")

    # so for the input "delete hello" the keyword will be delete
    input_keyword = input_string.split(" ")[0]
    # m = 50 + 0.05 this is the format for a variable definition

    if input_string == "variables":
        # show the list of variables
        print("Here's your list of variables:")
        for var in variables:
            value = variables[var].output_absolute()
            print(var + ": " + value)

    elif input_keyword == "delete":
        # delete a variable
        variable_to_delete = input_keyword = input_string.split(" ")[1]
        if variable_to_delete in variables:
            del variables[variable_to_delete]
            print("successfully deleted " + variable_to_delete + "!")
        else:
            print(variable_to_delete + " not found.")

    elif '=' in input_string:
        # if the definition is in the format m = a + b, where a and b are both Values
        var_name = get_variable_name(input_string)
        definition_body = get_definition_body(input_string)
        print("definition_body: " + definition_body)

        if is_num_definition(definition_body):
            # is the definition is in the form
            act_val_string = get_actual_value(definition_body)
            uncertainty_val_string = get_uncertainty_value(definition_body)

            # trying to convert the values into floats.
            try:
                uncertainty_val = float(uncertainty_val_string)
                act_val = float(act_val_string)

                # setting the variables!!!!
                set_variable_name(var_name, Values(act_val, uncertainty_val))

                print(var_name + " set! It has a value of " +
                      Values(act_val, uncertainty_val).output_absolute())

            except ValueError:
                print("Please type in valid values")

        else:
            # the definition is built on top of other variables
            # this means the definition_body is just an equation to parse

            print("parsing will be ready soon!")

    elif '+' or '-' or '/' or '*' or '**' in input_string:
        # if it's just an equation

        equation = input_string.split(" ")
        print("implemented soon!")

    else:
        print("not implemented yet lol")

    main()


main()
