import math
from Values import Values
from Uncertainties import *


def is_simple(str_in):
    check_str = str_in
    print("is_simple? " + str(check_str))
    global variables
    try:
        if check_str in variables:
            print("true")
            return True
    except:
        try:
            if int(check_str):
                print("true")
                return True
        except:
            print("false")
            return False
    try:
        int(check_str)
        print("true")
        return True
    except:
        print("false")
        return False


def get_type(operand_str):
    #either float, int or Values
    if operand_str in variables:
        if isinstance(variables[operand_str], Values):
            return "Values"
        else:
            print("Please check the global variables dictionary for key " + operand_str)
    elif eval("isinstance(" + operand_str + ",int)"):
        return "int"
    elif eval("isinstance(" + operand_str + ",float)"):
        return "float"
    else:
        print(operand_str + " Is not a Values, int or float. " + "Is type " + str(type(operand_str)) + "?")
            

def convert_operands(operand_str, operand_type):
    if operand_type == "Values":
        #try to get dictionary to store actual Values not str
        return variables[operand_str]
    elif operand_type == "int":
        return int(operand_str)
    elif operand_type == "float":
        return float(operand_str)
    else:
        print("Somehow the type of " + operand_str + "isn't float, int or Values, it's " + operand_type)


def Values_and_number(values, number, oper):
    if oper == "+" or oper == "-":
        actual = eval(str(values.actual) + oper + str(number))
        ans = Values(actual, values.absolute_unc)
        return ans
    elif oper == "*":
        ans = scale(values, number)
        return ans
    elif oper == "/":
        ans = scale(values, 1 / number)
        return ans
    elif oper == "^":
        ans = power(values, number)
        return ans
    else:
        print("Error at values_and_number function.")
        print("Oper is " + oper + " and values is " + values.output_absolute() + ". Number is " + str(number))


def solve_simple(tuple_in):
    str_operand1 = tuple_in[0][0]
    str_operand2 = tuple_in[0][1]
    oper          = tuple_in[1]
    operand1_type = get_type(str_operand1)
    operand2_type = get_type(str_operand2)
    operand1      = convert_operands(str_operand1, operand1_type)
    operand2      = convert_operands(str_operand2, operand2_type)
    char_to_oper  = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "^": power
    }

    if operand1_type == "float" or operand1_type == "int":
        if operand2_type == "float" or operand2_type == "int":
            if oper == "^":
                ans = pow(operand1, operand2)
                return ans
            else:
                ans = eval(str_operand1 + oper + str_operand2)
                return ans
        elif operand2_type == "Values":
            result = Values_and_number(operand2, operand1, oper)
            variables[str_operand2] = result
            return str_operand2
    elif operand1_type == "Values":
        if operand2_type == "float" or operand2_type == "int":
            result = Values_and_number(operand1, operand2, oper)
            variables[str_operand1] = result
            return str_operand1
        elif operand2_type == "Values":
            result = char_to_oper[oper](operand1, operand2)
            variables[str_operand1] = result
            return str_operand1
            

def simplify(tuple_in):
    operand1 = tuple_in[0][0]
    operand2 = tuple_in[0][1]
    oper     = tuple_in[1]
    print("Operand1 in the simplify func is: " + str(operand1) + " Operand2: " + str(operand2))
   
    if is_simple(operand1) and is_simple(operand2):
        return solve_simple(tuple_in)
    else:
        new_operand1 = operand1
        new_operand2 = operand2
        if not is_simple(operand1):
            new_operand1 = simplify(operand1)
        if not is_simple(operand2):
            new_operand2 = simplify(operand2)
        operands = [new_operand1, new_operand2]
        new_tuple = (operands, oper)
        return simplify(new_tuple)


variables = {
    "m1": Values(3, 1),
    "v": Values(6, 0.5)
}


input_tuple = ([(["m1","v"],"*"), "m1"], "+")
print(variables[simplify(input_tuple)].output_absolute())
