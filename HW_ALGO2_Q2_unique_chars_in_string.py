# Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.
# Hint: https://www.w3schools.com/python/python_sets.asp

def unique_chars_in_string(s):
    print("string = ", s)
    # initialize dictionary with keys from string and values default to 0
    newdict = dict.fromkeys(s, 0)
    # loop through string
    for x in s:
        # get the value for key x
        y = newdict.get(x)
        # increment y
        y += 1
        # when y = 2 then print message and return
        if y > 1:
            print("First non-unique character: ", x)
            return(False)
        else:
            newdict[x] = y
        print("key = ", x, " value = ", y)
    print("all characters in string are unique")
    return (True)

unique_chars_in_string('abcdefgh')