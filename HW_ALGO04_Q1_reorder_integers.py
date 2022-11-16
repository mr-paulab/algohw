# ALGO HW 4
# Q1
# Even First
# Your input is a list of integers, and you have to reorder its entries so that the even entries appear first.
# You are required to solve it without allocating additional storage (operate with the input list).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]
#
def reorder_even_first(input_list):
    print("Input list = ", input_list)
    count = 0
    for i in input_list:
#       if number is odd
        if input_list[count] % 2 != 0:
            popped = input_list.pop(count)
            input_list.append(popped)
        else:
            count += 1
    print("Final Sorted list = ", input_list)
    print("")
    return input_list

reorder_even_first([7, 3, 5, 6, 4, 10, 3, 2])
reorder_even_first([1, 2, 3, 4, 5, 6, 7, 8])
reorder_even_first([0, 1, 2, 3, 4, 5, 6, 7, 8])
reorder_even_first([0, 2, 4, 6, 8, 10, 12])
reorder_even_first([1, 3, 5, 7, 9, 11, 13])
reorder_even_first([91, 92, 93, 94, 95, 96, 97, 98, 99, 100])
reorder_even_first([-37, 22, 55, -56, 55, 19, 30, 22])