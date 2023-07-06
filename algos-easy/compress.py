# Compress

# Write a function, compress, that takes in a string as an argument. 
# The function should return a compressed version of the string where consecutive occurrences of 
# the same characters are compressed into the number of occurrences followed by the character. 
# Single character occurrences should not be changed.

# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'

# You can assume that the input only contains alphabetic characters.

# Two Pointer solution
# i = 0 -> end (tracks the letter)
# j = 0 -> end (tracks occurrences)

def compress(s):
    s += '.'
    # initialize a list to store result
    result = [] # -> ['2', 'c', '3', 'a', ]
    i, j = 0, 0

    # while loop to iterate thru string
    while j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            letter_count = j - i # int
            if letter_count == 1:
                result.append(s[i])
            else:
                result.append(str(letter_count))
                result.append(s[i])
            i = j

    print(result)
    return ''.join(result)

# TEST CASES
print(compress('ccaaatsss')) # -> '2c3at3s'
# compress('ssssbbz') # -> '4s2bz'
# compress('ppoppppp') # -> '2po5p'
# compress('nnneeeeeeeeeeeezz') # -> '3n12e2z'
# compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy');  # -> '127y'
