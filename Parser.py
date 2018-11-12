import math
from Values import Values
from Uncertainties import *


def is_Values(str_operand):
    try:
        print(str_operand + " is a Value(). It equals " +
              eval(str_operand) + ".output_absolute()")
        return True
    except Exception as e:
        # print(str_operand)
        # print(str_operand + " is not a Value(). Throwing exception: " + str(e))
        print((str_operand) +
              " is not a Value().")
        return False


def lowest_operation(str_in):

    order_of_opers = {
        "start": 10,
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3
    }

    total_opers = 0
    curr_lowest = "start"
    total_same = 0

    char_list = [ch for ch in str_in]
    char_list.reverse()
    for ch in char_list:
        if ch in "+-*/^":
            total_opers += 1
            if order_of_opers[ch] < order_of_opers[curr_lowest]:
                curr_lowest = ch
            elif order_of_opers[ch] == order_of_opers[curr_lowest]:
                total_same += 1

    if total_opers > 1:
        return curr_lowest
    elif total_opers == 1:
        return "one"
    elif total_opers == 0:
        return "zero"
    else:
        print("error on the lowest operation function")
        return "failure"


# eval_two takes in two values or constants with an operator and outputs the actual value.
def eval_two(str_in):
    # find operation used
    oper = "start"
    for ch in str_in:
        if ch in "+-*/^":
            oper = ch
    if oper == "start":
        print("Error help: eval_two didn't find an operation in" + str_in)
        return "error!"

    char_to_oper = {
        "+": "add",
        "-": "subtract",
        "*": "multiply",
        "/": "divide",
        "^": "power"
    }

    # getting the operands

    # operand_one - gets everything before operation
    operand_one = str_in.split(oper)[0].strip()

    # opernad two - everything after operation
    operand_two = str_in.split(oper)[1].strip()

    # checking to see is a value is a Value type (has an uncertainty)

    def evaluate_operation(function, oper_one, oper_two):
        return eval(function + "(" + str(oper_one) + "," + str(oper_two) + ")")

    if is_Values(operand_one) and is_Values(operand_two):
        try:
            ans = evaluate_operation(
                char_to_oper[oper], operand_one, operand_two)
            return ans
        except Exception as e:
            return "Maybe not implemented yet. Threw error " + e + "when evaluating the two Values " + operand_one + " and " + operand_two

    elif is_Values(operand_one) and (not is_Values(operand_two)):
        # operand one is a Value, operand two is a number
        f_operand_two = float(operand_two)
        if oper == '+':
            new_actual = operand_one.actual + f_operand_two
            return eval("Values(" + new_actual + "," + operand_one.absolute_unc + ")")
        elif oper == '-':
            new_actual = operand_one.actual - f_operand_two
            return eval("Values(" + new_actual + "," + operand_one.absolute_unc + ")")
        elif oper == '*':
            return evaluate_operation("scale", operand_one, f_operand_two)
        elif oper == '/':
            return evaluate_operation("scale", operand_one, (1 / f_operand_two))
        elif oper == '^':
            return evaluate_operation("power", operand_one, f_operand_two)
        else:
            print("operation not supported or not found.")

    elif (not is_Values(operand_one)) and is_Values(operand_two):
        # operand one is a number, operand two is a Value
        f_operand_one = float(operand_one)
        if oper == '+':
            new_actual = f_operand_one + operand_two.actual
            return eval("Values(" + new_actual + "," + operand_two.absolute_unc + ")")
        elif oper == '-':
            new_actual = f_operand_one - operand_two.actual
            return eval("Values(" + new_actual + "," + operand_two.absolute_unc + ")")
        elif oper == '*':
            return evaluate_operation("scale", operand_two, f_operand_one)
        elif oper == '/':
            return evaluate_operation("scale", operand_two, (1 / f_operand_one))
        else:
            return "error when trying " + oper + " on " + operand_one + " and " + operand_two

    else:
        # both are numbers
        return eval(operand_one + oper + operand_two)


def split_expression(str_in):
    first_oper = lowest_operation(str_in)
    if first_oper == "zero":
        return str_in
    elif first_oper == "one":
        # placeholder
        return eval_two(str_in)
    else:
        # splitting on the last occurence (rplit() is like reverse split)
        split_expression_array = str_in.rsplit(first_oper, 1)
        eval_str_1 = split_expression(split_expression_array[0].strip())
        eval_str_2 = split_expression(split_expression_array[1].strip())
        final_str = str(eval_str_1) + first_oper + str(eval_str_2)
        return eval_two(final_str)


test_string = "Values(20, 0.1) / 2 + Values(10, 0.3)"
print(split_expression(test_string).output_absolute())
