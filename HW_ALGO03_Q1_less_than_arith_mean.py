# ALGO HW 3
# Q1
# When given a list, the program should return a list of all the elements below the original list’s arithmetical mean.
# The arithmetical mean is the sum of all elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]
#
def less_than_arith_mean(input_list):
    print("Input list = ", input_list)
    mean = 0
    y = 0
    count = 0
    for x in input_list:
        y += int(x)
        count += 1
    mean = y/count
    print("number of values = ", count, ", sum of values = ", y, ", arithmetic mean = ",mean)
    output_list = []
    output_list = [x for x in input_list if x < mean]
    print("Output list = ", output_list)
    print("")
    return output_list


less_than_arith_mean([1, 3, 5, 6, 4, 10, 2, 3])
less_than_arith_mean([4, 4, 4, 4, 4])
less_than_arith_mean([5, 5, 5, 5, 6])
less_than_arith_mean([5, 5, 5, 5, 4])
