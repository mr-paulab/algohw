# HW ALGO04 Question 2
#
# Increment a Number
# Write a program that takes as input a list of digits encoding a nonnegative decimal integer D
# and updates the list to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].
#
# Note: same number of digits maintained from input to output

def increment_number(input_list):
    print("Input list = ", input_list)
    temp_string = ''
    temp_int = 0
    number_after = 0
    for x in input_list:
        temp_string += str(x)
    temp_int = int(temp_string)
    number_after = temp_int + 1
    output_list = [int(x) for x in str(number_after)]
    while len(output_list) < len(temp_string):
        output_list = [0] + output_list
    print("Output list after increment = ", output_list)
    print("")
    return(output_list)

increment_number([1, 2, 9])
increment_number([9, 9, 9])
increment_number([0, 0, 0])
increment_number([0, 0, 8])
increment_number([1, 0, 0, 0])
increment_number([0, 0, 0, 0, 0, 0, 0, 7])
increment_number([0, 0, 0, 0, 0, 0, 0, 9])