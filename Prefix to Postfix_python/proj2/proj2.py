from proj2.mylist import MyList
from proj2.mylist import Node

# This file processes each line of the input file and provides
# a corresponding postfix expression or an error code as output

# Function below determines if the postfix expression has characters
# other than letters and operators. If it only contains letters and operators
# returns True, otherwise returns False.
# Param: List of characters


def valid_char(expression):
    count = 0
    for x in expression:
        if str(x) in ['+', '-', '*', '/', '$', '\n'] or ('a' <= str(x) <= "z") or ('A' <= str(x) <= "Z"):
            count += 1
    if count == len(expression):
        return True
    else:
        return False


# Function below evaluates if the expression is valid based on
# whether it has the correct operand to operator ratio
# If it has an operator count that is equal to one less than the operand count
# returns True, otherwise returns False.
# param: list of characters


def valid_expression(expression):
    x = 0
    y = 0
    for ele in expression:
        if str(ele) in ['+', '-', '*', '/', '$']:
            x += 1
        elif ('a' <= str(ele) <= 'z') or ('A' <= str(ele) <= "Z"):
            y += 1
    if x == (y - 1):
        return True
    else:
        return False


# This function determines if the expression is in prefix notation.
# In the event that a postfix or infix expression is given as input, this
# function will return false.
# param: list of characters


def valid_prefix(expression):
    if str(expression[0]) not in ['+', '-', '*', '/', '$']:
        return False
    else:
        return True


# This function treats extra whitespace if it is given in the input expression
# This makes sure that the expression will still evaluate if it has spaces in it
# returns a list with no spaces
# param: list of characters


def treat_spaces(expression):
    new_str = ""
    str2 = ""
    for ele in expression:
        new_str += str(ele)
    for i in range(0, len(new_str)):
        if new_str[i] != " ":
            str2 += new_str[i]
    new_list = MyList()
    new_list.string_to_list(str2)
    return new_list


# this function is a recursive function that processes a prefix expression
# and returns the expression in postfix form. If a character is an operator
# the function will call itself, if it is an operand, it gets assigned to
# a variable. The final output is then converted to a string so it can be
# written to the output file.


def pre_to_post(exp):
    x = exp.remove_head()
    y = pre_to_post(exp) if exp[0] in ['+', '-', '*', '/', '$'] else exp.remove_head()
    z = pre_to_post(exp) if exp[0] in ['+', '-', '*', '/', '$'] else exp.remove_head()
    res = [y, z, x]
    st1 = ""
    for ele in res:
        st1 += str(ele)
    return st1


# Reads given input file line by line using a while loop until no more lines
# are left. In the while loop, the line is passed through a series of if
# statements that check the integrity of the expression using the functions
# above. If the expression is deemed valid, it is then passed through the
# pre to post recursive function. The output from each expression read is
# written to the output file.
# param input_file: An opened text file set to read mode
# param output_file: An opened text file set to write mode


def process_files(input_file, output_file):
    next_line = input_file.readline()
    while next_line is not None and next_line != "":
        prefix = MyList()
        prefix.string_to_list(str(next_line))
        prefix = treat_spaces(prefix)
        output_file.write("Input: \n")
        output_file.write(str(next_line) + '\n')
        output_file.write("Output: \n")
        if valid_char(prefix) is False:
            output_file.write("Error: Invalid character in expression")
        elif valid_expression(prefix) is False:
            output_file.write("Error: Incorrect number of operators or operands")
        elif valid_prefix(prefix) is False:
            output_file.write("Error: Only prefix expressions accepted")
        else:
            output_file.write(pre_to_post(prefix))
        output_file.write('\n\n\n')
        next_line = input_file.readline()
