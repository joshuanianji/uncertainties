import math
from Values import Values
from Uncertainties import *
from Parser import eval_expression, return_answer

# this is the file that deals with a user interface. When we are finished we'll make this file Main.py file.


# global variables dictionary
variables = {}


def set_variable(var_name, a, b):
    # variables[name] = "Value(a, b)"
    variables.update({var_name: "Values(" + str(a) + "," + str(b) + ")"})
    # eval("variables[" + str(var_name) + "] = " + str(value))


# # takes in a variable name, outputs Values(a, b)
def get_variable_value(var_name):
    if var_name in variables:
        var_value_string = variables.get(var_name, "Variable not found!")

        # var_value_string should be in the form "Values(a, b)"
        return var_value_string
    else:
        print(var_name + " not found in as a variable!")
        return "No value found!!"


def get_variable_name_from_input(str_in):
    # everything before the equals sign
    variable_name = str_in.split("=")[0].strip().replace(' ', '_')
    return variable_name


def get_definition_body_from_input(str_in):
    # everything after the equals sign lmao
    definition_body = str_in.split("=")[1].strip()
    return definition_body


def get_actual_value_from_input(str_in):
    # gets everything before the plus sign
    actual_value = str_in.split("+")[0].strip()
    return actual_value


def get_uncertainty_value(str_in):
    # everything after the plus sign
    return str_in.split("+")[1].strip()

# this is used for detecting variable definitions


def is_num_definition(str_in):
    # if the definition is in the format m = a + b, where a and b are both user inputted c + d values
    try:
        string_test = str_in.replace('+', '').replace(' ', '').replace('.', '')
        return string_test.isdigit()
    except IndexError:
        # is there aren't any spaces or dots or plus signs
        return False


print("> Set a variable or type out an equation.")
print("> To set a variable in absolute uncertainty form please type it out in the format m = 50 + 0.05 where m is the variable name, 50 is the value, and 0.05 is the absolute uncertainty.")
print("please note any spaces in variable names will be replaced with an underscore")


# this searches through the the variables dictionary and replaces the variable names with Values(a,b)
# I can't just use a regular string.replace(new, old)
def replace_variables(input_string):

    for key, value in variables.items():
        if key in input_string:
            print(key + " found in " + input_string +
                  ", replacing it with " + value)
            input_string = input_string.replace(key, value)
        else:
            print(key + " not found in " + input_string)

    return input_string


def main():
    input_string = input(">")

    # so for the input "delete hello" the keyword will be delete
    input_keyword = input_string.split(" ")[0]
    # m = 50 + 0.05 this is the format for a variable definition

    if input_string == "variables":
        # show the list of variables
        print("Here's your list of variables:")
        for var in variables:
            value = return_answer(get_variable_value(var))
            value_raw = get_variable_value(var)
            print(var + ": " + value_raw + " (" + value + ")")

    elif input_keyword == "delete":
        # delete a variable
        variable_to_delete = input_keyword = input_string.split(" ")[1]
        if variable_to_delete in variables:
            del variables[variable_to_delete]
            print("successfully deleted " + variable_to_delete + "!")
        else:
            print(variable_to_delete + " not found.")

    elif '=' in input_string:
        # if we're making a variable equal something
        var_name = get_variable_name_from_input(input_string)
        definition_body = get_definition_body_from_input(input_string)
        print("definition_body: " + definition_body)

        if is_num_definition(definition_body):
            # if the definition is in the format m = a + b, where a and b are both user inputted c + d values

            try:
                # if these don't work it means that the variable definition is not in the form of "a + b"
                act_val_string = get_actual_value_from_input(definition_body)
                uncertainty_val_string = get_uncertainty_value(definition_body)

                # if this doesn't work the values aren't valid
                uncertainty_val = float(uncertainty_val_string)
                act_val = float(act_val_string)

                # setting the variables!!!!
                set_variable(var_name, str(act_val), str(uncertainty_val))

                print(var_name + " set! It has a value of " +
                      get_variable_value(var_name))

            except ValueError:
                print("Please type in valid values")

            except IndexError:
                print("Bad format!")

        else:
            # the definition is built on top of other variables
            # this means the definition_body is just an equation to parse

            print("Expression detected! We are replacing the variables...")
            new_input = replace_variables(input_string)
            print(new_input)

            try:
                answer = eval_expression(new_input)
                print("Wow it worked! The answer is: " + answer)
                # answer will be in the string form "Values(a, b)" so if I wanted the a and b values I have to evaluate the Values(a, b) myself
                act_val = eval(answer + ".actual")
                absolute_unc = eval(answer + ".absolute_unc")

                # setting the variables!!!!
                set_variable(var_name, str(act_val), str(uncertainty_val))

                print(var_name + " set! It has a value of " +
                      get_variable_value(var_name))

            except Exception as e:
                print("Lol it didn't work. Outputted " + str(e))

    elif '+' or '-' or '/' or '*' or '**' in input_string:
        # if it's just an expression
        print("Expression detected! We are replacing the variables...")
        new_input = replace_variables(input_string)
        print("We replaced the variables and the new input is: " + str(new_input))

        try:
            answer = eval_expression(new_input)
            print("Wow it worked! The answer is: " + return_answer(answer))
        except Exception as e:
            print("Lol it didn't work Outputted " + str(e))

    else:
        print("not implemented yet lol")

    main()


main()
