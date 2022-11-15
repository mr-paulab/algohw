# ALGO HW 3
# Q2
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3
#
def find_two_lowest_elements(input_list):

    print("Input list = ", input_list)
    input_list.sort()
    print("Sorted list = ", input_list)
    list_lowest = []
    list_lowest.append(input_list[0])
    list_lowest.append(input_list[1])
    print("Output list (two lowest values) = ", list_lowest)
    print("")
    return list_lowest

find_two_lowest_elements([198, 3, 4, 9, 10, 9, 2])
find_two_lowest_elements([4, 0, 0, 9, 10, 9, 2])