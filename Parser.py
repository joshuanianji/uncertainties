import math
from Values import Values
from Uncertainties import *


def is_Values(str_operand):
    try:
        operand_value = eval(str_operand + ".output_absolute()")
        return True
    except:
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

    # operand two - everything after operation
    operand_two = str_in.split(oper)[1].strip()

    def evaluate_operation(function, oper_one, oper_two):
        ans = eval(function + "(" + str(oper_one) + "," + str(oper_two) + ")")
        return ans.output_self()

    # checking to see is a value is a Value type (has an uncertainty)
    if is_Values(operand_one) and is_Values(operand_two):
        try:
            ans = evaluate_operation(
                char_to_oper[oper], operand_one, operand_two)
            return ans
        except Exception as e:
            print("Maybe not implemented yet. Threw error '" + str(e) + "' when evaluating the two Values: " +
                  operand_one + " and " + operand_two + ". This is on line 88.")

    elif is_Values(operand_one) and (not is_Values(operand_two)):
        # operand one is a Value, operand two is a number
        ac_operand_one = eval(operand_one + ".actual")
        unc_operand_one = eval(operand_one + ".absolute_unc")
        f_operand_two = float(operand_two)

        if oper == '+':
            new_actual = ac_operand_one + f_operand_two
            sum = eval("Values(" + str(new_actual) +
                       "," + str(unc_operand_one) + ")")
            return sum.output_self()
        elif oper == '-':
            new_actual = ac_operand_one - f_operand_two
            return eval("Values(" + str(new_actual) + "," + str(unc_operand_one) + ")")
        elif oper == '*':
            return evaluate_operation("scale", operand_one, f_operand_two)
        elif oper == '/':
            return evaluate_operation("scale", operand_one, (1 / f_operand_two))
        elif oper == '^':
            return evaluate_operation("power", operand_one, f_operand_two)
        else:
            print("Operation '" + oper +
                  "' not supported or not found on line 1112")

    elif (not is_Values(operand_one)) and is_Values(operand_two):
        # operand one is a number, operand two is a Value
        ac_operand_two = eval(operand_two + ".actual")
        unc_operand_two = eval(operand_two + ".absolute_unc")
        f_operand_one = float(operand_one)

        if oper == '+':
            new_actual = f_operand_one + ac_operand_two
            return eval("Values(" + str(new_actual) + "," + str(unc_operand_two) + ")").output_self()
        elif oper == '-':
            new_actual = f_operand_one - ac_operand_two
            return eval("Values(" + str(new_actual) + "," + str(unc_operand_two) + ")").output_self()
        elif oper == '*':
            return evaluate_operation("scale", operand_two, f_operand_one)
        elif oper == '/':
            return evaluate_operation("scale", operand_two, (1 / f_operand_one))
        else:
            return "error when trying " + oper + " on " + operand_one + " and " + operand_two + " on line 131."

    else:
        # both are numbers
        if oper in "+-*/":
            return str(eval(operand_one + oper + operand_two))
        elif oper == "^":
            return str(eval(operand_one + "**" + operand_two))


def split_expression(str_in):
    first_oper = lowest_operation(str_in)
    if first_oper == "zero":
        return str_in
    elif first_oper == "one":
        # placeholder
        return eval_two(str_in)
    else:

        # helper functions to find things inside brackets
        def inside_brackets(string_in_thingy):
            before_first_bracket = string_in_thingy.split('[')[0].strip()
            after_second_bracket = string_in_thingy.split(']')[1].strip()

            after_first_bracket = string_in_thingy.split('[')[1].strip()
            inside_bracket_string = after_first_bracket.split(']')[0].strip()

            return [before_first_bracket, inside_bracket_string, after_second_bracket]

        # checking if the string contains brackets
        contains_brackets = False
        for ch in str_in:
            if ch in "[":
                contains_brackets = True

        if contains_brackets:
            expression_list = inside_brackets(str_in)
            # run split_expression for the stuff inside the brackets - just
            return split_expression(expression_list[0] + split_expression(expression_list[1]) + expression_list[2])
        else:
            # splitting on the last occurence (rplit() is like reverse split)
            split_expression_array = str_in.rsplit(first_oper, 1)
            eval_str_1 = split_expression(split_expression_array[0].strip())
            eval_str_2 = split_expression(split_expression_array[1].strip())
            final_str = str(eval_str_1) + first_oper + str(eval_str_2)
            return eval_two(final_str)


# if it's a number return the number. if it's a Value return its output_absolute() function.
def return_answer(thingy):
    if is_Values(thingy):
        return eval(thingy + ".output_absolute()")
    else:
        return thingy


# returns the answer as Values(a, b) in a string
def eval_selected(string):
    return eval(split_expression(string) + ".output_self()")


test_string = "[3 + 2 - 7] / 2 + Values(3, 4)"

result = split_expression(test_string)

print(return_answer(result))
