# Split in half
#Given a string. Split it into two equal parts. Swap these parts and return the result.
#If the string has odd characters, the first part should be one character greater than the second part.
#Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.
#
def split_string_and_swap_parts(input_string):
    print("Input string = ", input_string)
    if len(input_string) % 2 == 0:
        fsubstring_len = int(len(input_string)/2)
        ssubstring_len = int(len(input_string)/2)
    else:
        fsubstring_len = int(((len(input_string))+1)/2)
        ssubstring_len = int(((len(input_string))-1)/2)
    first_half = input_string[0:fsubstring_len]
    second_half = input_string[-ssubstring_len:]
    swap = second_half
    second_half = first_half
    first_half = swap
    output_string = first_half + second_half
    print("Output string = ", output_string)

split_string_and_swap_parts('AAAaBBB')




